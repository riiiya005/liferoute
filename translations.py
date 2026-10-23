"""
LifeRoute Translation Dictionary
Contains complete English and natural, idiomatic Bangla translations for the entire application.
"""

TRANSLATIONS = {
    "en": {
        # Brand & Global
        "brand_name": "LifeRoute",
        "brand_tagline": "Every Minute Matters",
        "prototype": "Emergency care availability, matched to your needs",
        "disclaimer_short": "Important: LifeRoute helps match patients to available emergency facilities based on capability. It does not provide medical advice.",
        "disclaimer_full": "LifeRoute is not a medical provider, diagnostic tool, or live verified hospital network. In a life-threatening emergency, please call 999 immediately or go to the nearest emergency room.",
        "emergency_helpline": "Emergency Hotline: 999",

        # Navigation
        "home": "Home",
        "emergency": "Emergency Care",
        "hospitals": "Hospitals",
        "ambulance": "Ambulance",
        "blood": "Find Blood",
        "medicine": "Find Medicine",
        "about": "About",
        "menu": "Menu",
        "close": "Close",

        # Quick Actions & Common Buttons
        "find_care": "Find Emergency Care",
        "find_ambulance": "Find Ambulance",
        "find_blood": "Find Blood",
        "find_medicine": "Find Medicine",
        "call": "Call",
        "call_now": "Call Now",
        "call_pharmacy": "Call Pharmacy",
        "route": "View Route",
        "open_route_maps": "Open route in Google Maps",
        "share": "Share Emergency Plan",
        "share_plan": "Share Plan",
        "copy_details": "Copy emergency details",
        "copied_details": "Copied to clipboard!",
        "share_via_apps": "Share emergency plan",
        "back_to_results": "Back to Match Results",
        "search": "Search",
        "filter": "Filter",
        "clear": "Clear",
        "available": "Available",
        "unavailable": "Unavailable",
        "available_now": "Available now",
        "currently_unavailable": "Currently unavailable",
        "beds_available": "beds available",
        "units_available": "units listed",
        "packs_available": "packs listed",
        "km_away": "km away",
        "best": "BEST MATCH",
        "nearest_available": "NEAREST AVAILABLE",
        "try_demo": "Accident & Trauma Care: Emergency readiness and blood check in Uttara",

        # Quick Scenario Section
        "quick_scenario_eyebrow": "RAPID EMERGENCY ASSESSMENT",
        "quick_scenario_title": "Tell us what’s happening",
        "quick_scenario_desc": "Choose the symptoms or situation that best describes the emergency.",
        "scenario_accident_title": "Severe Trauma / Road Accident",
        "scenario_accident_desc": "Uttara · Evaluates emergency trauma center, ICU availability, and O+ blood",
        "scenario_accident_action": "Evaluate Available Care",
        "scenario_chest_title": "Chest Pain / Cardiac Care",
        "scenario_breathing_title": "Severe Respiratory Distress",
        "scenario_view_all": "All Emergency Situations",

        # Live Triage Demo Realistic Status
        "live_triage_badge": "LIVE HOSPITAL AVAILABILITY",
        "live_status_updated": "Updated just now",
        "live_best_match": "CURRENT BEST MATCH",
        "live_hospital_name": "Hospital B",
        "live_hospital_sub": "Uttara Emergency Care Center",
        "live_facility_meta": "Government · Uttara · 1.2 km",
        "live_check_emergency": "Emergency care available",
        "live_check_icu": "ICU available",
        "live_check_beds": "18 beds available",
        "live_check_blood": "O+ blood available",
        "why_this_match": "WHY THIS MATCH?",
        "why_match_desc": "Matches the required emergency resources and is currently available.",
        "availability_verified": "Availability checked just now with facility dispatch",
        "live_hospital_b_caption": "Hospital B · Uttara Emergency Care Center",

        # Hero & Home Page
        "hero_eyebrow": "SMART EMERGENCY CARE MATCHING",
        "hero_title": "When every minute matters, find care that's actually available.",
        "hero_title_main": "When every minute matters,",
        "hero_title_sub": "find care that's actually available.",
        "hero_lead": "LifeRoute helps you find suitable emergency care based on what you need and what is available now, not distance alone.",
        "hero_art_caption": "Care, when it counts",
        "how_eyebrow": "HOW LIFEROUTE WORKS",
        "how_title": "A clearer path during an emergency",
        "how_lead": "Traditional navigation apps only measure distance. LifeRoute verifies emergency readiness and specialized care before guiding you.",
        
        # Steps
        "step_1_title": "Tell us what happened",
        "step_1_desc": "Select the emergency situation with simple, calm choices.",
        "step_2_title": "Understand care needed",
        "step_2_desc": "Determines emergency triage level, ICU, and blood requirements.",
        "step_3_title": "Check available hospitals",
        "step_3_desc": "Verifies emergency capacity, vacant beds, and on-hand blood units.",
        "step_4_title": "Find a suitable hospital",
        "step_4_desc": "Ranks hospitals by capability first, then proximity.",
        "step_5_title": "Get there & share plan",
        "step_5_desc": "One-tap navigation in Google Maps and instant caregiver coordination.",

        # Features / Why LifeRoute
        "why_title": "Why suitability comes before distance",
        "feat_1_title": "Capability First",
        "feat_1_desc": "A hospital 1 km away cannot help if its ICU is full or blood bank is dry. We filter by readiness first.",
        "feat_2_title": "Integrated Resources",
        "feat_2_desc": "Ambulance contacts, donor networks, and emergency pharmacy stock right when you need them.",
        "feat_3_title": "Instant Action",
        "feat_3_desc": "Direct phone dialing, Google Maps navigation routes, and shareable summaries in one touch.",

        # Emergency Intake Form
        "intake_eyebrow": "EMERGENCY TRIAGE",
        "intake_title": "Let's find the right next step.",
        "intake_subtitle": "This short guide cannot diagnose a condition. If someone is in immediate danger, seek emergency medical care now.",
        "progress_step_1": "Situation",
        "progress_step_2": "Details",
        "progress_step_3": "Matching",
        "progress_step_4": "Action Plan",
        
        "legend_situation": "What is happening?",
        "legend_details": "A few quick triage details",
        "label_area": "Current area",
        "label_conscious": "Are they conscious?",
        "label_breathing": "Difficulty breathing?",
        "label_bleeding": "Heavy bleeding?",
        "label_chest": "Chest pain?",
        "label_blood": "Blood group (if known)",
        
        "opt_conscious_yes": "Yes / I'm not sure",
        "opt_conscious_no": "No (Unconscious)",
        "opt_breathing_no": "No / Breathing normally",
        "opt_breathing_yes": "Yes (Severe distress)",
        "opt_bleeding_no": "No / Minor bleeding",
        "opt_bleeding_yes": "Yes (Heavy bleeding)",
        "opt_chest_no": "No / None",
        "opt_chest_yes": "Yes (Severe pressure/pain)",
        "opt_blood_unknown": "Not known",

        # Situations
        "sit_accident": "Road Accident",
        "sit_bleeding": "Heavy Bleeding",
        "sit_breathing": "Trouble Breathing",
        "sit_chest": "Chest Pain",
        "sit_pregnancy": "Pregnancy Emergency",
        "sit_burn": "Serious Burn",
        "sit_unconscious": "Person is Unconscious",
        "sit_other": "Something Else",

        # Results Page
        "results_eyebrow": "YOUR CARE MATCH",
        "critical_alert": "Critical emergency. Please seek emergency medical care immediately.",
        "moderate_alert": "This may require urgent medical attention.",
        "low_alert": "Please consider medical care if symptoms continue or worsen.",
        "looked_for": "Based on what you shared, we looked for:",
        "including_blood": "including {blood} blood",
        "why_hospital": "Why this hospital?",
        "reason_emergency": "Required emergency care is available",
        "reason_icu": "ICU is available",
        "reason_beds": "Beds are available",
        "reason_blood": "Required blood is available",
        "reason_suitability": "Suitable before distance is considered",
        "map_title": "Interactive Route & Facilities Map",
        "empty_results_title": "We couldn't find a suitable hospital with all required care right now.",
        "empty_results_desc": "Try contacting an emergency ambulance directly or check alternative facilities below.",
        "other_hospitals": "Other Hospitals Evaluated",
        "not_suitable": "Not currently suitable",
        "suitable_match": "Suitable match",

        # Hospitals Directory
        "hospitals_eyebrow": "HOSPITAL DIRECTORY",
        "hospitals_title": "Find care across Dhaka",
        "hospitals_subtitle": "Fictional demonstration facilities and sample availability only.",
        "search_hospital_placeholder": "Hospital name or area",
        "filter_area": "Area",
        "filter_type": "Type",
        "filter_sort": "Sort",
        "all_areas": "All Areas",
        "all_types": "All",
        "government": "Government",
        "private": "Private",
        "sort_best": "Best Match",
        "sort_nearest": "Nearest Suitable",
        "sort_beds": "Most Beds Available",
        "no_hospitals_found": "No hospitals found matching your search criteria.",
        "services_label": "Services available:",

        # Ambulance Page
        "ambulance_eyebrow": "AMBULANCE SUPPORT",
        "ambulance_title": "Need an ambulance?",
        "ambulance_subtitle": "Find a nearby available ambulance contact for your area. Availability is demonstration data; call to confirm.",
        "filter_select_area": "Select area",
        "sort_ambulance_nearest": "Nearest",
        "sort_ambulance_available": "Available Now",
        "sort_ambulance_area": "Area",
        "find_nearest_ambulance": "Find nearest ambulance",
        "alt_phone": "Alt",

        # Blood Page
        "blood_eyebrow": "BLOOD SUPPORT",
        "blood_title": "Find blood support nearby",
        "blood_subtitle": "Availability is demonstration data. Please call to confirm before travelling.",
        "select_blood_group": "Select blood group",
        "hospital_blood_banks": "Hospital Blood Banks",
        "community_donors": "Community Volunteer Donors",
        "no_blood_units": "No matching blood units listed right now.",
        "community_fallback_note": "Community volunteers in the selected area may still be able to help.",
        "no_donors": "No matching community volunteers are listed in this area.",
        "units_count": "units listed",

        # Pharmacy Page
        "pharmacy_eyebrow": "MEDICINE AVAILABILITY",
        "pharmacy_title": "Find the medicine you need",
        "pharmacy_subtitle": "This is an availability search, not medical advice. Demonstration stock should be confirmed by phone.",
        "medicine_search_placeholder": "e.g. Napa, Paracetamol, Omeprazole",
        "search_label": "Medicine name, brand or generic",
        "available_matches": "Available matches",
        "nearby_matches": "Nearby area results",
        "no_medicine_found": "We couldn't find this medicine in the selected area.",
        "no_medicine_hint": "Try another spelling, generic name, or select a nearby area.",
        "search_prompt_title": "Search by medicine, brand, or generic name.",
        "search_prompt_subtitle": "For example: Napa, Paracetamol, Seclo, or Omeprazole.",
        "quick_searches": "Common searches:",
        "generic": "Generic",
        "strength": "Strength",
        "form": "Form",

        # About Page
        "about_eyebrow": "ABOUT LIFEROUTE",
        "about_title": "Nearest isn't always the right hospital.",
        "about_lead": "Traditional maps can show nearby hospitals. LifeRoute goes further by considering the emergency and the care currently available before recommending a suitable place to go.",
        "about_p1_title": "Made for people, not dashboards",
        "about_p1_desc": "Emergency decisions are stressful. LifeRoute uses plain language to help make the next step clearer and avoid frantic guesswork.",
        "about_p2_title": "Honest by design",
        "about_p2_desc": "This is a humanitarian prototype using fictional demonstration data. It does not claim a live network, a confirmed bed, or guaranteed admission.",
        "about_p3_title": "Suitability before distance",
        "about_p3_desc": "A nearby facility is only helpful if it can support the care someone needs. The matching engine checks relevant care before ranking the options.",
        "about_vision_title": "Our Vision for Dhaka",
        "about_vision_desc": "In dense urban environments like Dhaka, traffic congestion and mismatched hospital capability cost precious lives. LifeRoute demonstrates an intelligent, capability-aware routing paradigm that connects patients to ready hospitals, reducing diversion and critical delays.",

        # Share Page
        "share_eyebrow": "EMERGENCY SHARE PLAN",
        "share_badge": "LIFEROUTE EMERGENCY PLAN",
        "share_title": "{level} emergency support plan",
        "share_summary": "Emergency details prepared for patient transfer and family communication.",
        "plan_area": "Area:",
        "plan_needs": "Care needed:",
        "plan_blood": "Blood group:",
        "plan_hospital": "Recommended Hospital:",
        "plan_contact": "Emergency Phone:",
        "plan_distance": "Estimated Distance:",
        "plan_instructions": "Directions: Tap 'Open route in Google Maps' for turn-by-turn navigation.",

        # Care Needs Labels
        "need_emergency": "Emergency Care",
        "need_icu": "ICU",
        "need_beds": "Available Beds",
        "need_blood": "Required Blood",

        # Severity Levels
        "critical": "Critical",
        "moderate": "Moderate",
        "low": "Low",

        # Footer
        "footer_tagline": "Emergency care navigation and hospital readiness network for Dhaka.",
        "footer_links": "Quick Links",
        "footer_notice": "LifeRoute Emergency Care Network · Not medical advice · Always dial 999 in life-threatening emergencies.",
        "all_rights": "LifeRoute Emergency Care Platform. Designed for rapid emergency response."
    },

    "bn": {
        # Brand & Global
        "brand_name": "লাইফরুট",
        "brand_tagline": "প্রতিটি মিনিট গুরুত্বপূর্ণ",
        "prototype": "জরুরি সেবার প্রাপ্যতা, আপনার প্রয়োজনের সাথে সামঞ্জস্যপূর্ণ",
        "disclaimer_short": "জরুরি তথ্য: লাইফরুট রোগীর প্রয়োজন অনুযায়ী হাসপাতালের সেবার সক্ষমতা যাচাই করে। এটি কোনো সরাসরি চিকিৎসা পরামর্শ নয়।",
        "disclaimer_full": "লাইফরুট কোনো চিকিৎসা প্রদানকারী, ডায়াগনস্টিক মাধ্যম বা সরাসরি পরীক্ষিত হাসপাতাল নেটওয়ার্ক নয়। জীবনের ঝুঁকি থাকলে অবিলম্বে ৯৯৯ নম্বরে কল করুন বা নিকটস্থ জরুরি বিভাগে যান।",
        "emergency_helpline": "জরুরি হটলাইন: ৯৯৯",

        # Navigation
        "home": "হোম",
        "emergency": "জরুরি সেবা",
        "hospitals": "হাসপাতাল",
        "ambulance": "অ্যাম্বুলেন্স",
        "blood": "রক্ত খুঁজুন",
        "medicine": "ওষুধ খুঁজুন",
        "about": "পরিচিতি",
        "menu": "মেনু",
        "close": "বন্ধ করুন",

        # Quick Actions & Common Buttons
        "find_care": "জরুরি সেবা খুঁজুন",
        "find_ambulance": "অ্যাম্বুলেন্স খুঁজুন",
        "find_blood": "রক্ত খুঁজুন",
        "find_medicine": "ওষুধ খুঁজুন",
        "call": "কল করুন",
        "call_now": "এখনই কল করুন",
        "call_pharmacy": "ফার্মেসিতে কল করুন",
        "route": "রুট দেখুন",
        "open_route_maps": "গুগল ম্যাপে রুট দেখুন",
        "share": "জরুরি পরিকল্পনা শেয়ার করুন",
        "share_plan": "পরিকল্পনা শেয়ার",
        "copy_details": "জরুরি বিবরণ কপি করুন",
        "copied_details": "ক্লিপবোর্ডে কপি করা হয়েছে!",
        "share_via_apps": "জরুরি পরিকল্পনা শেয়ার করুন",
        "back_to_results": "ফলাফলে ফিরে যান",
        "search": "খুঁজুন",
        "filter": "ফিল্টার",
        "clear": "মুছুন",
        "available": "উপলব্ধ",
        "unavailable": "অনুপলব্ধ",
        "available_now": "এখন উপলব্ধ",
        "currently_unavailable": "বর্তমানে অনুপলব্ধ",
        "beds_available": "টি শয্যা খালি",
        "units_available": "ইউনিট মজুত রয়েছে",
        "packs_available": "প্যাক মজুত রয়েছে",
        "km_away": "কিমি দূরে",
        "best": "সেরা মিল",
        "nearest_available": "নিকটতম উপলব্ধ",
        "try_demo": "সড়ক দুর্ঘটনা ও জরুরি ট্রমা সেবা: উত্তরায় সক্ষমতা ও রক্ত প্রাপ্যতা যাচাই",

        # Quick Scenario Section
        "quick_scenario_eyebrow": "তাৎক্ষণিক জরুরি মূল্যায়ন",
        "quick_scenario_title": "কী ঘটেছে তা জানান",
        "quick_scenario_desc": "উপসর্গ বা জরুরি পরিস্থিতি অনুযায়ী বিকল্পটি বেছে নিন যাতে সঠিক সেবা নিশ্চিত করা যায়।",
        "scenario_accident_title": "গুরুতর আঘাত / সড়ক দুর্ঘটনা",
        "scenario_accident_desc": "উত্তরা · জরুরি ট্রমা কেয়ার, আইসিইউ এবং ও-পজিটিভ রক্ত প্রাপ্যতা যাচাই",
        "scenario_accident_action": "সেবার সক্ষমতা যাচাই করুন",
        "scenario_chest_title": "বুকে তীব্র ব্যথা / হৃদরোগ",
        "scenario_breathing_title": "তীব্র শ্বাসকষ্ট",
        "scenario_view_all": "সকল জরুরি পরিস্থিতি",

        # Live Triage Demo Realistic Status
        "live_triage_badge": "সরাসরি হাসপাতালের সক্ষমতা",
        "live_status_updated": "এইমাত্র যাচাইকৃত",
        "live_best_match": "বর্তমান সেরা মিল",
        "live_hospital_name": "হাসপাতাল বি",
        "live_hospital_sub": "উত্তরা জরুরি চিকিৎসা কেন্দ্র",
        "live_facility_meta": "সরকারি · উত্তরা · ১.২ কিমি",
        "live_check_emergency": "জরুরি সেবা উপলব্ধ",
        "live_check_icu": "আইসিইউ উপলব্ধ",
        "live_check_beds": "১৮টি শয্যা খালি",
        "live_check_blood": "ও+ রক্ত উপলব্ধ",
        "why_this_match": "কেন এই হাসপাতাল?",
        "why_match_desc": "রোগীর প্রয়োজনীয় জরুরি সুবিধা (জরুরি বিভাগ, আইসিইউ ও ও-পজিটিভ রক্ত) বিদ্যমান এবং এই মুহূর্তে সেবা দিতে সক্ষম।",
        "availability_verified": "হাসপাতাল নিয়ন্ত্রণ কক্ষের মাধ্যমে এইমাত্র প্রাপ্যতা নিশ্চিত করা হয়েছে",
        "live_hospital_b_caption": "হাসপাতাল বি · উত্তরা জরুরি চিকিৎসা কেন্দ্র",

        # Hero & Home Page
        "hero_eyebrow": "স্মার্ট জরুরি চিকিৎসা ম্যাচিং",
        "hero_title": "যখন প্রতিটি মিনিট গুরুত্বপূর্ণ, তখন নিশ্চিত সেবা খুঁজুন।",
        "hero_title_main": "যখন প্রতিটি মিনিট গুরুত্বপূর্ণ,",
        "hero_title_sub": "তখন নিশ্চিত সেবা খুঁজুন।",
        "hero_lead": "লাইফরুট কেবল দূরত্বের ওপর নির্ভর না করে রোগীর প্রয়োজন এবং হাসপাতালের বর্তমান সেবার সক্ষমতা যাচাই করে উপযুক্ত হাসপাতাল খুঁজে দেয়।",
        "hero_art_caption": "সঙ্কটের মুহূর্তে সঠিক সেবা",
        "how_eyebrow": "লাইফরুট কীভাবে কাজ করে",
        "how_title": "জরুরি পরিস্থিতিতে সঠিক দিকনির্দেশনা",
        "how_lead": "সাধারণ ম্যাপ কেবল দূরত্ব মাপে। লাইফরুট হাসপাতালে যাওয়ার আগেই জরুরি চিকিৎসা, আইসিইউ এবং রক্তের প্রাপ্যতা যাচাই করে।",
        
        # Steps
        "step_1_title": "কী ঘটেছে তা জানান",
        "step_1_desc": "সহজ কয়েকটি বিকল্পের মাধ্যমে জরুরি পরিস্থিতি নির্বাচন করুন।",
        "step_2_title": "চিকিৎসার ধরন নির্ধারণ",
        "step_2_desc": "জরুরি বিভাগ, আইসিইউ কিংবা রক্তের প্রয়োজনীয়তা স্বয়ংক্রিয়ভাবে নির্ধারণ হয়।",
        "step_3_title": "হাসপাতালের সক্ষমতা যাচাই",
        "step_3_desc": "হাসপাতালের জরুরি বিভাগ, খালি শয্যা এবং ব্লাড ব্যাংকের মজুত যাচাই করা হয়।",
        "step_4_title": "সঠিক হাসপাতাল বাছাই",
        "step_4_desc": "দূরত্বের চেয়ে চিকিৎসা দেওয়ার সক্ষমতাকে সর্বোচ্চ অগ্রাধিকার দিয়ে তালিকা করা হয়।",
        "step_5_title": "গন্তব্যে যাত্রা ও শেয়ার",
        "step_5_desc": "এক ক্লিকে গুগল ম্যাপে দিকনির্দেশনা ও স্বজনদের কাছে পরিকল্পনা পাঠানোর সুবিধা।",

        # Features / Why LifeRoute
        "why_title": "দূরত্বের আগে কেন সেবার সক্ষমতা জরুরি",
        "feat_1_title": "সক্ষমতাই প্রথম",
        "feat_1_desc": "মাত্র ১ কিমি কাছের হাসপাতালও কোনো কাজে আসবে না যদি সেখানে আইসিইউ বা রক্তের ব্যবস্থা না থাকে। আমরা সক্ষমতা আগে যাচাই করি।",
        "feat_2_title": "সমন্বিত জরুরি সেবা",
        "feat_2_desc": "জরুরি অ্যাম্বুলেন্স, স্বেচ্ছাসেবী রক্তদাতা এবং ২৪ ঘণ্টার ফার্মেসির তথ্য এক জায়গায়।",
        "feat_3_title": "তাৎক্ষণিক যোগাযোগ",
        "feat_3_desc": "সরাসরি ফোন কল, গুগল ম্যাপে রুট এবং স্বজনদের সাথে সহজে শেয়ারের সুযোগ।",

        # Emergency Intake Form
        "intake_eyebrow": "জরুরি সেবা অনুসন্ধান",
        "intake_title": "আসুন সঠিক পরবর্তী পদক্ষেপ খুঁজে নিই।",
        "intake_subtitle": "এই সংক্ষিপ্ত নির্দেশিকা কোনো রোগ নির্ণয় করে না। রোগী যদি তাৎক্ষণিক বিপদে থাকেন, তবে অবিলম্বে জরুরি চিকিৎসা নিন।",
        "progress_step_1": "পরিস্থিতি",
        "progress_step_2": "বিবরণ",
        "progress_step_3": "হাসপাতাল যাচাই",
        "progress_step_4": "দিকনির্দেশনা",
        
        "legend_situation": "কী ঘটেছে?",
        "legend_details": "কয়েকটি প্রয়োজনীয় তথ্য",
        "label_area": "বর্তমান এলাকা",
        "label_conscious": "রোগী কি সচেতন?",
        "label_breathing": "শ্বাস নিতে কি কষ্ট হচ্ছে?",
        "label_bleeding": "অতিরিক্ত রক্তক্ষরণ হচ্ছে?",
        "label_chest": "বুকে তীব্র ব্যথা বা চাপ আছে?",
        "label_blood": "রক্তের গ্রুপ (জানা থাকলে)",
        
        "opt_conscious_yes": "হ্যাঁ / নিশ্চিত নই",
        "opt_conscious_no": "না (অচেতন)",
        "opt_breathing_no": "না / স্বাভাবিক শ্বাসপ্রশ্বাস",
        "opt_breathing_yes": "হ্যাঁ (তীব্র শ্বাসকষ্ট)",
        "opt_bleeding_no": "না / রক্তপাত নেই",
        "opt_bleeding_yes": "হ্যাঁ (অতিরিক্ত রক্তক্ষরণ)",
        "opt_chest_no": "না / নেই",
        "opt_chest_yes": "হ্যাঁ (তীব্র চাপ বা ব্যথা)",
        "opt_blood_unknown": "জানা নেই",

        # Situations
        "sit_accident": "সড়ক দুর্ঘটনা",
        "sit_bleeding": "অতিরিক্ত রক্তক্ষরণ",
        "sit_breathing": "তীব্র শ্বাসকষ্ট",
        "sit_chest": "বুকে তীব্র ব্যথা",
        "sit_pregnancy": "গর্ভকালীন জরুরি অবস্থা",
        "sit_burn": "গুরুতর পোড়া",
        "sit_unconscious": "রোগী অচেতন",
        "sit_other": "অন্যান্য জরুরি অবস্থা",

        # Results Page
        "results_eyebrow": "আপনার জন্য উপযুক্ত সেবা",
        "critical_alert": "সংকটজনক জরুরি অবস্থা। অবিলম্বে জরুরি চিকিৎসা সেবা নিন।",
        "moderate_alert": "এটি জরুরি চিকিৎসা সেবা প্রয়োজন হতে পারে।",
        "low_alert": "লক্ষণ বজায় থাকলে বা বাড়লে চিকিৎসকের পরামর্শ নিন।",
        "looked_for": "আপনার তথ্যের ভিত্তিতে আমরা যা যাচাই করেছি:",
        "including_blood": "যার মধ্যে {blood} গ্রুপের রক্ত অন্তর্ভুক্ত",
        "why_hospital": "এই হাসপাতালটি কেন উপযুক্ত?",
        "reason_emergency": "প্রয়োজনীয় জরুরি সেবা চালু রয়েছে",
        "reason_icu": "আইসিইউ শয্যা উপলব্ধ রয়েছে",
        "reason_beds": "সাধারণ শয্যা খালি রয়েছে",
        "reason_blood": "প্রয়োজনীয় গ্রুপের রক্ত মজুত রয়েছে",
        "reason_suitability": "দূরত্ব বিবেচনার আগেই চিকিৎসাগত উপযুক্ততা যাচাইকৃত",
        "map_title": "ইন্টারেক্টিভ রুট ও হাসপাতাল মানচিত্র",
        "empty_results_title": "এই মুহূর্তে সব প্রয়োজনীয় সুবিধাসহ কোনো উপযুক্ত হাসপাতাল পাওয়া যায়নি।",
        "empty_results_desc": "একটি অ্যাম্বুলেন্সে যোগাযোগ করার চেষ্টা করুন অথবা বিকল্প সহায়তা গ্রহণ করুন।",
        "other_hospitals": "যাচাইকৃত অন্যান্য হাসপাতাল",
        "not_suitable": "বর্তমানে অনুপযুক্ত",
        "suitable_match": "উপযুক্ত হাসপাতাল",

        # Hospitals Directory
        "hospitals_eyebrow": "হাসপাতাল তালিকা",
        "hospitals_title": "ঢাকা শহরের হাসপাতাল ও জরুরি সেবা",
        "hospitals_subtitle": "প্রদর্শনী ও নমুনা তথ্য ভিত্তিক হাসপাতাল তালিকা।",
        "search_hospital_placeholder": "হাসপাতালের নাম বা এলাকা",
        "filter_area": "এলাকা",
        "filter_type": "ধরন",
        "filter_sort": "বাছাইক্রম",
        "all_areas": "সকল এলাকা",
        "all_types": "সব",
        "government": "সরকারি",
        "private": "বেসরকারি",
        "sort_best": "সেরা মিল",
        "sort_nearest": "নিকটতম উপযুক্ত",
        "sort_beds": "সর্বাধিক খালি শয্যা",
        "no_hospitals_found": "আপনার অনুসন্ধান অনুযায়ী কোনো হাসপাতাল পাওয়া যায়নি।",
        "services_label": "উপলব্ধ সেবাসমূহ:",

        # Ambulance Page
        "ambulance_eyebrow": "জরুরি অ্যাম্বুলেন্স সেবা",
        "ambulance_title": "জরুরি অ্যাম্বুলেন্স প্রয়োজন?",
        "ambulance_subtitle": "আপনার এলাকার নিকটস্থ উপলব্ধ অ্যাম্বুলেন্সে যোগাযোগ করুন। কল করে প্রাপ্যতা নিশ্চিত করুন।",
        "filter_select_area": "এলাকা নির্বাচন করুন",
        "sort_ambulance_nearest": "নিকটতম",
        "sort_ambulance_available": "এখন উপলব্ধ",
        "sort_ambulance_area": "এলাকা অনুযায়ী",
        "find_nearest_ambulance": "নিকটতম অ্যাম্বুলেন্স খুঁজুন",
        "alt_phone": "বিকল্প",

        # Blood Page
        "blood_eyebrow": "জরুরি রক্ত সহায়তা",
        "blood_title": "নিকটস্থ ব্লাড ব্যাংক ও রক্তদাতা খুঁজুন",
        "blood_subtitle": "প্রদর্শনী তথ্য। যাওয়ার আগে অনুগ্রহ করে ফোনে নিশ্চিত হয়ে নিন।",
        "select_blood_group": "রক্তের গ্রুপ নির্বাচন করুন",
        "hospital_blood_banks": "হাসপাতাল ব্লাড ব্যাংক",
        "community_donors": "কমিউনিটি স্বেচ্ছাসেবী রক্তদাতা",
        "no_blood_units": "এই মুহূর্তে উপযুক্ত রক্তের ইউনিট তালিকাভুক্ত নেই।",
        "community_fallback_note": "নির্বাচিত এলাকার স্বেচ্ছাসেবী রক্তদাতারা সাহায্য করতে পারেন।",
        "no_donors": "এই এলাকায় কোনো স্বেচ্ছাসেবী তালিকাভুক্ত নেই।",
        "units_count": "ইউনিট মজুত রয়েছে",

        # Pharmacy Page
        "pharmacy_eyebrow": "জরুরি ওষুধ প্রাপ্যতা",
        "pharmacy_title": "প্রয়োজনীয় ওষুধ খুঁজুন",
        "pharmacy_subtitle": "এটি প্রাপ্যতা অনুসন্ধানের তথ্য, চিকিৎসকের পরামর্শ নয়। স্টকের তথ্য ফোনে নিশ্চিত করুন।",
        "medicine_search_placeholder": "যেমন: নাপা, প্যারাসিটামল, ওমিপ্রাজল",
        "search_label": "ওষুধের নাম, ব্র্যান্ড বা জেনেরিক",
        "available_matches": "উপলব্ধ ওষুধের তালিকা",
        "nearby_matches": "নিকটবর্তী এলাকার ফলাফল",
        "no_medicine_found": "নির্বাচিত এলাকায় এই ওষুধটি পাওয়া যায়নি।",
        "no_medicine_hint": "অন্য বানান দিয়ে চেষ্টা করুন, জেনেরিক নাম লিখুন বা পার্শ্ববর্তী এলাকা নির্বাচন করুন।",
        "search_prompt_title": "ওষুধের নাম, ব্র্যান্ড বা জেনেরিক নাম লিখে খুঁজুন।",
        "search_prompt_subtitle": "যেমন: নাপা, প্যারাসিটামল, সেক্লো বা ওমিপ্রাজল।",
        "quick_searches": "জনপ্রিয় অনুসন্ধান:",
        "generic": "জেনেরিক",
        "strength": "মাত্রা",
        "form": "ধরন",

        # About Page
        "about_eyebrow": "লাইফরুট পরিচিতি",
        "about_title": "সবচেয়ে কাছের হাসপাতালটি সবসময় সঠিক নাও হতে পারে।",
        "about_lead": "সাধারণ ম্যাপ কেবল কাছের হাসপাতাল দেখায়। লাইফরুট আরও এক ধাপ এগিয়ে রোগীর জরুরি অবস্থা এবং বর্তমানে উপলব্ধ সক্ষমতা যাচাই করে সবচেয়ে উপযুক্ত হাসপাতালের সন্ধান দেয়।",
        "about_p1_title": "মানুষের জরুরি প্রয়োজনের কথা ভেবে তৈরি",
        "about_p1_desc": "জরুরি মুহূর্তে সঠিক সিদ্ধান্ত নেওয়া অত্যন্ত কঠিন। লাইফরুট সহজ ভাষায় পরিষ্কার দিকনির্দেশনা দেয় যাতে কোনো ধরনের দ্বিধাদ্বন্দ্ব তৈরি না হয়।",
        "about_p2_title": "স্বচ্ছ ও বাস্তবসম্মত",
        "about_p2_desc": "এটি একটি মানবিক প্রোটোটাইপ যা নমুনা তথ্য ব্যবহার করে। এটি সরাসরি নিশ্চিত ভর্তি বা লাইভ নেটওয়ার্কের দাবি করে না, বরং একটি আদর্শ ব্যবস্থার রূপরেখা তুলে ধরে।",
        "about_p3_title": "দূরত্বের আগে সক্ষমতা যাচাই",
        "about_p3_desc": "কাছের হাসপাতাল কেবল তখনই কার্যকর যখন সেখানে রোগীর প্রয়োজনীয় সেবাটি পাওয়া যায়। আমাদের ম্যাচিং সিস্টেম প্রয়োজনীয় সেবা নিশ্চিত করে তারপর তালিকা প্রস্তুত করে।",
        "about_vision_title": "ঢাকার জন্য আমাদের দৃষ্টিভঙ্গি",
        "about_vision_desc": "ঢাকার মতো ঘনবসতিপূর্ণ শহরে যানজট এবং ভুল হাসপাতালে যাওয়ার কারণে রোগীর অমূল্য জীবন বিপন্ন হয়। লাইফরুট এমন একটি সক্ষমতা-ভিত্তিক জরুরি নেভিগেশন প্রদর্শন করে যা রোগীদের সরাসরি উপযুক্ত হাসপাতালে পৌঁছে দেয়।",

        # Share Page
        "share_eyebrow": "জরুরি শেয়ার পরিকল্পনা",
        "share_badge": "লাইফরুট জরুরি পরিকল্পনা",
        "share_title": "{level} জরুরি সহায়তা পরিকল্পনা",
        "share_summary": "রোগী স্থানান্তর ও স্বজনদের সাথে দ্রুত যোগাযোগের জন্য প্রস্তুতকৃত জরুরি বিবরণ।",
        "plan_area": "এলাকা:",
        "plan_needs": "প্রয়োজনীয় সেবা:",
        "plan_blood": "রক্তের গ্রুপ:",
        "plan_hospital": "সুপারিশকৃত হাসপাতাল:",
        "plan_contact": "জরুরি ফোন নম্বর:",
        "plan_distance": "আনুমানিক দূরত্ব:",
        "plan_instructions": "দিকনির্দেশনা: গুগল ম্যাপে ধাপে ধাপে রুট দেখতে 'গুগল ম্যাপে রুট দেখুন' বাটনে চাপ দিন।",

        # Care Needs Labels
        "need_emergency": "জরুরি সেবা",
        "need_icu": "আইসিইউ",
        "need_beds": "খালি শয্যা",
        "need_blood": "প্রয়োজনীয় রক্ত",

        # Severity Levels
        "critical": "সংকটজনক",
        "moderate": "মাঝারি",
        "low": "কম",

        # Footer
        "footer_tagline": "ঢাকার জন্য জরুরি স্বাস্থ্যসেবা নেভিগেশন ও সক্ষমতা যাচাই নেটওয়ার্ক।",
        "footer_links": "প্রয়োজনীয় লিংক",
        "footer_notice": "লাইফরুট জরুরি সেবা নেটওয়ার্ক · চিকিৎসকের বিকল্প নয় · অতি জরুরি মুহূর্তে ৯৯৯ নম্বরে কল করুন।",
        "all_rights": "লাইফরুট জরুরি সেবা প্ল্যাটফর্ম। দ্রুত জরুরি চিকিৎসা সহায়তার জন্য নির্মিত।"
    }
}

# Translation mappings for database values
AREA_TRANSLATIONS = {
    "en": {
        "All Areas": "All Areas",
        "Uttara": "Uttara",
        "Mirpur": "Mirpur",
        "Dhanmondi": "Dhanmondi",
        "Gulshan": "Gulshan",
        "Banani": "Banani",
        "Mohammadpur": "Mohammadpur",
        "Mohakhali": "Mohakhali",
        "Farmgate": "Farmgate",
        "Badda": "Badda",
        "Rampura": "Rampura",
        "Jatrabari": "Jatrabari",
        "Old Dhaka": "Old Dhaka"
    },
    "bn": {
        "All Areas": "সকল এলাকা",
        "Uttara": "উত্তরা",
        "Mirpur": "মিরপুর",
        "Dhanmondi": "ধানমন্ডি",
        "Gulshan": "গুলশান",
        "Banani": "বনানী",
        "Mohammadpur": "মোহাম্মদপুর",
        "Mohakhali": "মহাখালী",
        "Farmgate": "ফার্মগেট",
        "Badda": "বাড্ডা",
        "Rampura": "রামপুরা",
        "Jatrabari": "যাত্রাবাড়ী",
        "Old Dhaka": "পুরান ঢাকা"
    }
}

KIND_TRANSLATIONS = {
    "en": {
        "All": "All",
        "Government": "Government",
        "Private": "Private"
    },
    "bn": {
        "All": "সব",
        "Government": "সরকারি",
        "Private": "বেসরকারি"
    }
}

SORT_TRANSLATIONS = {
    "en": {
        "Best Match": "Best Match",
        "Nearest Suitable": "Nearest Suitable",
        "Most Beds Available": "Most Beds Available",
        "Nearest": "Nearest",
        "Available Now": "Available Now",
        "Area": "Area"
    },
    "bn": {
        "Best Match": "সেরা মিল",
        "Nearest Suitable": "নিকটতম উপযুক্ত",
        "Most Beds Available": "সর্বাধিক খালি শয্যা",
        "Nearest": "নিকটতম",
        "Available Now": "এখন উপলব্ধ",
        "Area": "এলাকা অনুযায়ী"
    }
}

SERVICE_TYPE_TRANSLATIONS = {
    "en": {
        "Basic life support": "Basic Life Support",
        "Patient transport": "Patient Transport"
    },
    "bn": {
        "Basic life support": "বেসিক লাইফ সাপোর্ট",
        "Patient transport": "সাধারণ রোগী পরিবহন"
    }
}

DOSAGE_TRANSLATIONS = {
    "en": {
        "Tablet": "Tablet",
        "Capsule": "Capsule",
        "Inhaler": "Inhaler",
        "Injection": "Injection",
        "Sachet": "Sachet"
    },
    "bn": {
        "Tablet": "ট্যাবলেট",
        "Capsule": "ক্যাপসুল",
        "Inhaler": "ইনহেলার",
        "Injection": "ইনজেকশন",
        "Sachet": "স্যাচেট"
    }
}

NEEDS_TRANSLATIONS = {
    "en": {
        "Emergency Care": "Emergency Care",
        "ICU": "ICU",
        "Available Beds": "Available Beds",
        "Required Blood": "Required Blood"
    },
    "bn": {
        "Emergency Care": "জরুরি সেবা",
        "ICU": "আইসিইউ",
        "Available Beds": "খালি শয্যা",
        "Required Blood": "প্রয়োজনীয় রক্ত"
    }
}

STATUS_REASONS_TRANSLATIONS = {
    "en": {
        "Emergency care is currently unavailable": "Emergency care is currently unavailable",
        "ICU is currently unavailable": "ICU is currently unavailable",
        "No beds are currently listed as available": "No beds are currently listed as available",
        "blood is not currently listed as available": "blood is not currently listed as available"
    },
    "bn": {
        "Emergency care is currently unavailable": "জরুরি সেবা বর্তমানে বন্ধ রয়েছে",
        "ICU is currently unavailable": "আইসিইউ বর্তমানে অনুপলব্ধ",
        "No beds are currently listed as available": "বর্তমানে কোনো শয্যা খালি নেই",
        "blood is not currently listed as available": "রক্ত বর্তমানে মজুত নেই"
    }
}
