// [GLOTO] Global Configuration
window.GLOTO = window.GLOTO || {};

// 1. Language Metadata (순서 및 기본 설정)
window.GLOTO.LANG_META = {
    // 1-8: Priority
    'ko': { name: 'Korean', native: '한국어', geo: 'kr', tts: 'ko-KR' },
    'vn': { name: 'Vietnamese', native: 'Tiếng Việt', geo: 'vn', tts: 'vi-VN' },
    'cn': { name: 'Chinese', native: '中文', geo: 'cn', tts: 'zh-CN' },
    'th': { name: 'Thai', native: 'ภาษาไทย', geo: 'th', tts: 'th-TH' },
    'ph': { name: 'Filipino', native: 'Filipino', geo: 'ph', tts: 'tl-PH' },
    'id': { name: 'Indonesian', native: 'Bahasa Indonesia', geo: 'id', tts: 'id-ID' },
    'mn': { name: 'Mongolian', native: 'Монгол хэл', geo: 'mn', tts: 'mn-MN' },
    'uz': { name: 'Uzbek', native: 'Oʻzbek tili', geo: 'uz', tts: 'uz-UZ' },

    // 9-14: Expansion
    'ne': { name: 'Nepali', native: 'नेपाली', geo: 'np', tts: 'ne-NP' },
    'km': { name: 'Khmer', native: 'ភាសាខ្មែរ', geo: 'kh', tts: 'km-KH' },
    'si': { name: 'Sinhala', native: 'සිංහල', geo: 'lk', tts: 'si-LK' },
    'my': { name: 'Burmese', native: 'ဗမာစာ', geo: 'mm', tts: 'my-MM' },
    'bn': { name: 'Bengali', native: 'বাংলা', geo: 'bd', tts: 'bn-BD' },
    'lo': { name: 'Lao', native: 'ພາສາລາວ', geo: 'la', tts: 'lo-LA' },

    // 15-18: Global/Bridge
    'ru': { name: 'Russian', native: 'Русский', geo: 'ru', tts: 'ru-RU' },
    'en': { name: 'English', native: 'English', geo: 'us', tts: 'en-US' },
    'jp': { name: 'Japanese', native: '日本語', geo: 'jp', tts: 'ja-JP' },
    'kz': { name: 'Kazakh', native: 'Қазақ тілі', geo: 'kz', tts: 'kk-KZ' }
};

// 2. Study Box Categories
window.GLOTO.CATEGORIES = {
    'School': { icon: '🏫', default: 'School' },
    'Travel': { icon: '✈️', default: 'Travel' },
    'Hospital': { icon: '🏥', default: 'Hospital' },
    'Market': { icon: '🛒', default: 'Market' },
    'Restaurant': { icon: '🍽️', default: 'Restaurant' },
    'Airport': { icon: '🛫', default: 'Airport' }
};

// 3. Global Data Storage (Populated by locale files)
window.GLOTO.DATA = {}; // Structure: { ko: { ui: {}, content: { School: [] } }, en: ... }
