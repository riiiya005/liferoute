/**
 * LifeRoute — Application JavaScript
 * Mobile Navigation, Leaflet Map Visualization, and Interactive Controls
 */

// Mobile Navigation Toggle
function toggleNav() {
  const nav = document.getElementById('siteNav');
  const btn = document.querySelector('.mobile-toggle');
  if (!nav) return;
  const isOpen = nav.classList.toggle('open');
  if (btn) {
    btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }
}

// Close mobile nav when clicking outside
document.addEventListener('click', (e) => {
  const nav = document.getElementById('siteNav');
  const btn = document.querySelector('.mobile-toggle');
  if (nav && nav.classList.contains('open') && !nav.contains(e.target) && !btn.contains(e.target)) {
    nav.classList.remove('open');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  }
});

// Leaflet Map Initialization
document.addEventListener('DOMContentLoaded', () => {
  const mapEl = document.querySelector('#map');
  if (!mapEl || typeof L === 'undefined') return;

  try {
    const hospitals = JSON.parse(mapEl.dataset.hospitals || '[]');
    if (!hospitals || !hospitals.length) return;

    const bestId = mapEl.dataset.bestId ? parseInt(mapEl.dataset.bestId, 10) : null;
    const bestHospital = hospitals.find(h => bestId ? h.id === bestId : h.suitable) || hospitals[0];

    // Initialize map centered at best hospital or Dhaka center
    const centerLat = bestHospital ? bestHospital.lat : 23.8759;
    const centerLng = bestHospital ? bestHospital.lng : 90.3795;
    const map = L.map('map', {
      scrollWheelZoom: false,
      zoomControl: true
    }).setView([centerLat, centerLng], 13);

    // OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors',
      maxZoom: 18
    }).addTo(map);

    const bounds = [];

    // Custom Icon Creators
    const createMarkerIcon = (isBest, isSuitable) => {
      let bgColor = isBest ? '#0f766e' : (isSuitable ? '#16a34a' : '#94a3b8');
      let symbol = isBest ? '★' : (isSuitable ? '+' : '✕');
      let size = isBest ? 38 : 30;
      let border = isBest ? '3px solid #ffffff' : '2px solid #ffffff';
      let shadow = isBest ? 'box-shadow: 0 4px 12px rgba(15,118,110,0.4);' : 'box-shadow: 0 2px 6px rgba(0,0,0,0.2);';

      return L.divIcon({
        className: 'custom-map-pin',
        html: `<div style="
          width: ${size}px;
          height: ${size}px;
          background: ${bgColor};
          border: ${border};
          ${shadow}
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          color: #ffffff;
          font-size: ${isBest ? '16px' : '13px'};
          font-weight: 700;
          cursor: pointer;
        ">${symbol}</div>`,
        iconSize: [size, size],
        iconAnchor: [size / 2, size / 2],
        popupAnchor: [0, -size / 2]
      });
    };

    hospitals.forEach(h => {
      const isBest = bestHospital && (h.id === bestHospital.id);
      const isSuitable = Boolean(h.suitable);
      const icon = createMarkerIcon(isBest, isSuitable);

      bounds.push([h.lat, h.lng]);

      const marker = L.marker([h.lat, h.lng], {
        icon: icon,
        zIndexOffset: isBest ? 1000 : (isSuitable ? 500 : 100)
      }).addTo(map);

      // Popup Content
      const popupHtml = `
        <div style="font-family: inherit; font-size: 13px; line-height: 1.4; padding: 4px;">
          <div style="font-weight: 800; font-size: 14px; color: #0f172a; margin-bottom: 4px;">
            ${isBest ? '<span style="display:inline-block; padding: 2px 6px; background: #0f766e; color: #ffffff; border-radius: 4px; font-size: 10px; font-weight: 800; letter-spacing: 0.05em; margin-bottom: 4px;">BEST MATCH</span><br>' : ''}${h.name}
          </div>
          <div style="color: #64748b; font-size: 12px; margin-bottom: 6px;">
            ${h.area} · ${h.distance || 0} km
          </div>
          <div style="font-size: 12px; margin-bottom: 8px;">
            <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-weight: 700; background: ${isSuitable ? '#f0fdf4; color: #15803d;' : '#fef2f2; color: #b91c1c;'}">
              ${isSuitable ? '✓ Suitable match' : '× Not suitable'}
            </span>
          </div>
          <div style="display:flex; gap: 6px;">
            <a href="tel:${h.phone}" style="background: #0f766e; color: #ffffff; padding: 5px 9px; border-radius: 4px; text-decoration: none; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center;">
              Call
            </a>
            <a href="https://www.google.com/maps/dir/?api=1&destination=${h.lat},${h.lng}" target="_blank" rel="noopener noreferrer" style="background: #f1f5f9; color: #334155; padding: 5px 9px; border-radius: 4px; text-decoration: none; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center;">
              Directions
            </a>
          </div>
        </div>
      `;

      marker.bindPopup(popupHtml);

      // Open best hospital popup by default
      if (isBest) {
        marker.openPopup();
      }
    });

    if (bounds.length > 1) {
      map.fitBounds(bounds, { padding: [40, 40], maxZoom: 14 });
    }
  } catch (err) {
    console.error('Error initializing hospital map:', err);
  }
});
