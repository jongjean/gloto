import os
import json

OUTPUT_DIR = '/var/www/gloto/js/locales'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. UI Text Data (Full 18 Languages)
UI_TEXT = {
     'ko': { 'appName': "우리하나", 'appDesc': "AI 세계어 배우기 앱", 'slogan': "우리는 하나", 'check': "확인", 'nativeLabel': "모국어", 'selectTarget': "어떤 언어를 배우시겠습니까?", 'title': "상황 선택", 'start': "시작하기", 'back': "뒤로", 'listening': "듣고 있어요...", 'placeholder': "마이크를 누르고 말하세요 ...", 'msgPerfect': "완벽해요! 🎉", 'msgGood': "좋아요! 👍", 'msgBad': "다시 한 번...", 'correction': "정답:", 'listen': "들어보기", 'why': "왜 틀렸을까요?", 'aiName': "AI 튜터", 
             'selectStep': "1. 상황 선택", 'speakStep': "2. 대화 연습",
             'btnFeedback': "의견 보내기", 'feedbackTitle': "사용자 의견", 'phFeedback': "불편한 점이나 의견을 남겨주세요.", 'phContact': "이름, 연락처 (이메일, 전화번호)", 'btnSend': "보내기", 'btnClose': "닫기", 'msgSent': "소중한 의견에 감사합니다. 더욱 나은 서비스로 보답하겠습니다.",
             'cat_School': "학교에서", 'cat_Travel': "여행에서", 'cat_Hospital': "병원에서", 'cat_Market': "시장에서", 'cat_Restaurant': "식당에서", 'cat_Airport': "공항에서" },
     'en': { 'appName': "GloTo", 'appDesc': "Global Language AI", 'slogan': "We Are One", 'check': "Check", 'nativeLabel': "Native Language", 'selectTarget': "Target Language", 'title': "Select Situation", 'start': "Start", 'back': "Back", 'listening': "Listening...", 'placeholder': "Tap mic & speak...", 'msgPerfect': "Perfect! 🎉", 'msgGood': "Good Job! 👍", 'msgBad': "Try Again...", 'correction': "Answer:", 'listen': "Listen", 'why': "Why?", 'aiName': "AI Tutor",
             'selectStep': "1. Select Situation", 'speakStep': "2. Speak Practice",
             'btnFeedback': "Send Feedback", 'feedbackTitle': "Feedback", 'phFeedback': "Leave your comments...", 'phContact': "Name, Contact (Email, Phone)", 'btnSend': "Send", 'btnClose': "Close", 'msgSent': "Sent successfully.",
             'cat_School': "School", 'cat_Travel': "Travel", 'cat_Hospital': "Hospital", 'cat_Market': "Market", 'cat_Restaurant': "Restaurant", 'cat_Airport': "Airport" },
     'vn': { 'appName': "GloTo", 'appDesc': "Học ngoại ngữ AI", 'slogan': "Chúng ta là một", 'check': "Kiểm tra", 'nativeLabel': "Ngôn ngữ mẹ đẻ", 'selectTarget': "Bạn muốn học tiếng gì?", 'title': "Chọn tình huống", 'start': "Bắt đầu", 'back': "Quay lại", 'listening': "Đang nghe...", 'placeholder': "Nhấn mic để nói...", 'msgPerfect': "Tuyệt vời! 🎉", 'msgGood': "Tốt lắm! 👍", 'msgBad': "Thử lại nào...", 'correction': "Đáp án:", 'listen': "Nghe", 'why': "Tại sao?", 'aiName': "Gia sư AI",
             'selectStep': "1. Chọn tình huống", 'speakStep': "2. Luyện nói",
             'btnFeedback': "Gửi ý kiến", 'feedbackTitle': "Ý kiến người dùng", 'phFeedback': "Nhập nội dung...", 'phContact': "Tên, Liên hệ (Email, SĐT)", 'btnSend': "Gửi", 'btnClose': "Đóng", 'msgSent': "Đã gửi.",
             'cat_School': "Trường học", 'cat_Travel': "Du lịch", 'cat_Hospital': "Bệnh viện", 'cat_Market': "Chợ", 'cat_Restaurant': "Nhà hàng", 'cat_Airport': "Sân bay" },
     'cn': { 'appName': "GloTo", 'appDesc': "AI语言学习", 'slogan': "我们是一体", 'check': "检查", 'nativeLabel': "母语", 'selectTarget': "选择目标语言", 'title': "选择场景", 'start': "开始", 'back': "返回", 'listening': "正在听...", 'placeholder': "按麦克风说话...", 'msgPerfect': "完美! 🎉", 'msgGood': "很好! 👍", 'msgBad': "再试一次...", 'correction': "答案:", 'listen': "听一听", 'why': "为什么?", 'aiName': "AI导师",
             'selectStep': "1. 选择场景", 'speakStep': "2. 口语练习",
             'btnFeedback': "反馈", 'feedbackTitle': "用户反馈", 'phFeedback': "请输入您的意见...", 'phContact': "姓名, 联系方式 (邮箱, 电话)", 'btnSend': "发送", 'btnClose': "关闭", 'msgSent': "已发送。",
             'cat_School': "学校", 'cat_Travel': "旅游", 'cat_Hospital': "医院", 'cat_Market': "市场", 'cat_Restaurant': "餐厅", 'cat_Airport': "机场" },
     'th': { 'appName': "GloTo", 'appDesc': "เรียนภาษา AI", 'slogan': "เราคือหนึ่งเดียว", 'check': "ตรวจ", 'nativeLabel': "ภาษาแม่", 'selectTarget': "เลือกภาษาที่คุณต้องการเรียน", 'title': "เลือกสถานการณ์", 'start': "เริ่ม", 'back': "กลับ", 'listening': "กำลังฟัง...", 'placeholder': "กดไมค์แล้วพูด...", 'msgPerfect': "ยอดเยี่ยม! 🎉", 'msgGood': "ดีมาก! 👍", 'msgBad': "ลองอีกครั้ง...", 'correction': "คำตอบ:", 'listen': "ฟัง", 'why': "ทำไม?", 'aiName': "ครูฝึก AI",
             'selectStep': "1. เลือกสถานการณ์", 'speakStep': "2. ฝึกพูด",
             'btnFeedback': "ส่งความคิดเห็น", 'feedbackTitle': "ความคิดเห็น", 'phFeedback': "กรุณาใส่ข้อความ...", 'phContact': "ชื่อ, ติดต่อ (อีเมล, โทรศัพท์)", 'btnSend': "ส่ง", 'btnClose': "ปิด", 'msgSent': "ส่งเรียบร้อยแล้ว",
             'cat_School': "โรงเรียน", 'cat_Travel': "การเดินทาง", 'cat_Hospital': "โรงพยาบาล", 'cat_Market': "ตลาด", 'cat_Restaurant': "ร้านอาหาร", 'cat_Airport': "สนามบิน" },
     'ph': { 'selectTarget': "Anong wika ang gusto mong matutunan?", 'cat_School': "Paaralan", 'cat_Travel': "Paglalakbay", 'cat_Hospital': "Ospital", 'cat_Market': "Palengke", 'cat_Restaurant': "Restawran", 'cat_Airport': "Paliparan", 'check': "Suriin", 'nativeLabel': "Katutubong Wika", 'selectStep': "1. Pumili ng sitwasyon", 'speakStep': "2. Magsanay magsalita", 'title': "Pumili ng Sitwasyon", 'start': "Magsimula", 'back': "Bumalik", 'listening': "Nakikinig...", 'placeholder': "Pindutin at magsalita...", 'msgPerfect': "Perpekto!", 'msgGood': "Magaling!", 'msgBad': "Subukan uli...", 'correction': "Sagot:", 'listen': "Makinig", 'why': "Bakit?", 'aiName': "AI Guro", 
             'btnFeedback': "Magbigay ng Opinyon", 'feedbackTitle': "Opinyon", 'phFeedback': "Mag-iwan ng komento...", 'phContact': "Pangalan, Kontak (Email, Telepono)", 'btnSend': "Ipadala", 'btnClose': "Isara", 'msgSent': "Naipadala na." },
     'id': { 'selectTarget': "Bahasa apa yang ingin Anda pelajari?", 'cat_School': "Sekolah", 'cat_Travel': "Perjalanan", 'cat_Hospital': "Rumah Sakit", 'cat_Market': "Pasar", 'cat_Restaurant': "Restoran", 'cat_Airport': "Bandara", 'check': "Cek", 'nativeLabel': "Bahasa Ibu", 'selectStep': "1. Pilih Situasi", 'speakStep': "2. Latihan Bicara", 'title': "Pilih Situasi", 'start': "Mulai", 'back': "Kembali", 'listening': "Mendengarkan...", 'placeholder': "Tekan dan bicara...", 'msgPerfect': "Sempurna!", 'msgGood': "Bagus!", 'msgBad': "Coba lagi...", 'correction': "Jawaban:", 'listen': "Dengar", 'why': "Kenapa?", 'aiName': "Guru AI",
             'btnFeedback': "Kirim Masukan", 'feedbackTitle': "Masukan Pengguna", 'phFeedback': "Tulis masukan Anda...", 'phContact': "Nama, Kontak (Email, Ponsel)", 'btnSend': "Kirim", 'btnClose': "Tutup", 'msgSent': "Terkirim." },
     'jp': { 'selectTarget': "どの言語を学びますか？", 'cat_School': "学校", 'cat_Travel': "旅行", 'cat_Hospital': "病院", 'cat_Market': "市場", 'cat_Restaurant': "レストラン", 'cat_Airport': "空港", 'check': "確認", 'nativeLabel': "母国語", 'selectStep': "1. 状況を選択", 'speakStep': "2. 会話練習", 'title': "状況を選択", 'start': "開始", 'back': "戻る", 'listening': "聞いています...", 'placeholder': "マイクを押して話す...", 'msgPerfect': "完璧です!", 'msgGood': "いいですね!", 'msgBad': "もう一度...", 'correction': "正解:", 'listen': "聞く", 'why': "解説", 'aiName': "AI先生",
             'btnFeedback': "意見を送る", 'feedbackTitle': "ユーザーの意見", 'phFeedback': "ご意見をお聞かせください...", 'phContact': "名前、連絡先 (メール、電話)", 'btnSend': "送信", 'btnClose': "閉じる", 'msgSent': "送信しました。" },
     'mn': { 'selectTarget': "Та ямар хэл сурмаар байна вэ?", 'cat_School': "Сургууль", 'cat_Travel': "Аялал", 'cat_Hospital': "Эмнэлэг", 'cat_Market': "Зах", 'cat_Restaurant': "Ресторан", 'cat_Airport': "Нисэх буудал", 'check': "Шалгах", 'nativeLabel': "Эх хэл", 'selectStep': "1. Нөхцөл сонгох", 'speakStep': "2. Ярианы дасгал", 'title': "Нөхцөл сонгох", 'start': "Эхлэх", 'back': "Буцах", 'listening': "Сонсож байна...", 'placeholder': "Ярина уу...", 'msgPerfect': "Гайхалтай!", 'msgGood': "Сайн байна!", 'msgBad': "Дахин оролдоно уу", 'correction': "Хариулт:", 'listen': "Сонсох", 'why': "Яагаад?", 'aiName': "AI Багш",
             'btnFeedback': "Санал илгээх", 'feedbackTitle': "Санал хүсэлт", 'phFeedback': "Саналаа бичнэ үү...", 'phContact': "Нэр, Холбоо барих (Имэйл, Утас)", 'btnSend': "Илгээх", 'btnClose': "Хаах", 'msgSent': "Илгээгдлээ." },
     'uz': { 'selectTarget': "Qaysi tilni o'rganmoqchisiz?", 'cat_School': "Maktab", 'cat_Travel': "Sayohat", 'cat_Hospital': "Kasalxona", 'cat_Market': "Bozor", 'cat_Restaurant': "Restoran", 'cat_Airport': "Aeroport", 'check': "Tekshirish", 'nativeLabel': "Ona tili", 'selectStep': "1. Vaziyatni tanlang", 'speakStep': "2. So'zlashuv mashqi", 'title': "Vaziyatni tanlang", 'start': "Boshlash", 'back': "Orqaga", 'listening': "Eshitilyapti...", 'placeholder': "Gapiring...", 'msgPerfect': "Ajoyib!", 'msgGood': "Yaxshi!", 'msgBad': "Qaytadan urinib ko'ring", 'correction': "Javob:", 'listen': "Tinglash", 'why': "Nega?", 'aiName': "AI O'qituvchi",
             'btnFeedback': "Fikr yuborish", 'feedbackTitle': "Fikr", 'phFeedback': "Fikringizni qoldiring...", 'phContact': "Ism, Aloqa (Email, Telefon)", 'btnSend': "Yuborish", 'btnClose': "Yopish", 'msgSent': "Yuborildi." },
     'ru': { 'selectTarget': "Какой язык вы хотите выучить?", 'cat_School': "Школа", 'cat_Travel': "Путешествие", 'cat_Hospital': "Больница", 'cat_Market': "Рынок", 'cat_Restaurant': "Ресторан", 'cat_Airport': "Аэропорт", 'check': "Проверить", 'nativeLabel': "Родной язык", 'selectStep': "1. Выберите ситуацию", 'speakStep': "2. Практика речи", 'title': "Выбор ситуации", 'start': "Начать", 'back': "Назад", 'listening': "Слушаю...", 'placeholder': "Говорите...", 'msgPerfect': "Отлично!", 'msgGood': "Хорошо!", 'msgBad': "Попробуйте еще", 'correction': "Ответ:", 'listen': "Послушать", 'why': "Почему?", 'aiName': "AI Репетитор",
             'btnFeedback': "Оставить отзыв", 'feedbackTitle': "Отзыв", 'phFeedback': "Напишите ваш отзыв...", 'phContact': "Имя, Контакты (Email, Телефон)", 'btnSend': "Отправить", 'btnClose': "Закрыть", 'msgSent': "Отправлено." },
     'kz': { 'selectTarget': "Қандай тіл үйренгіңіз келеді?", 'cat_School': "Мектеп", 'cat_Travel': "Саяхат", 'cat_Hospital': "Аурухана", 'cat_Market': "Базар", 'cat_Restaurant': "Мейрамхана", 'cat_Airport': "Әуежай", 'check': "Тексеру", 'nativeLabel': "Ана тілі", 'selectStep': "1. Жағдайды таңдаңыз", 'speakStep': "2. Сөйлесу жаттығуы", 'title': "Жағдайды таңдау", 'start': "Бастау", 'back': "Артқа", 'listening': "Тыңдап тұрмын...", 'placeholder': "Сөйлеңіз...", 'msgPerfect': "Тамаша!", 'msgGood': "Жақсы!", 'msgBad': "Қайта көріңіз", 'correction': "Жауап:", 'listen': "Тыңдау", 'why': "Неге?", 'aiName': "AI Мұғалім",
             'btnFeedback': "Пікір жіберу", 'feedbackTitle': "Пікір", 'phFeedback': "Пікіріңізді жазыңыз...", 'phContact': "Аты, Байланыс (Email, Телефон)", 'btnSend': "Жіберу", 'btnClose': "Жабу", 'msgSent': "Жіберілді." },
     'ne': { 'selectTarget': "तपाईं कुन भाषा सिक्न चाहनुहुन्छ?", 'cat_School': "विद्यालय", 'cat_Travel': "यात्रा", 'cat_Hospital': "अस्पताल", 'cat_Market': "बजार", 'cat_Restaurant': "रेस्टुरेन्ट", 'cat_Airport': "विमानस्थल", 'check': "जाँच्नुहोस्", 'nativeLabel': "मातृभाषा", 'selectStep': "1. परिस्थिति छान्नुहोस्", 'speakStep': "2. बोल्ने अभ्यास", 'title': "परिस्थिति छान्नुहोस्", 'start': "सुरु गर्नुहोस्", 'back': "फर्कनुहोस्", 'listening': "सुन्दै...", 'placeholder': "बोल्नुहोस्...", 'msgPerfect': "उत्कृष्ट!", 'msgGood': "राम्रो!", 'msgBad': "फेरि प्रयास गर्नुहोस्", 'correction': "उत्तर:", 'listen': "सुन्नुहोस्", 'why': "किन?", 'aiName': "AI शिक्षक",
             'btnFeedback': "सुझाव दिनुहोस्", 'feedbackTitle': "सुझाव", 'phFeedback': "विवरण लेख्नुहोस्...", 'phContact': "नाम, सम्पर्क (इमेल, फोन)", 'btnSend': "पठाउनुहोस्", 'btnClose': "बन्द गर्नुहोस्", 'msgSent': "पठाइयो।" },
     'km': { 'selectTarget': "តើអ្នកចង់រៀនភាសាអ្វី?", 'cat_School': "សាលារៀន", 'cat_Travel': "ការធ្វើដំណើរ", 'cat_Hospital': "មន្ទីរពេទ្យ", 'cat_Market': "ផ្សារ", 'cat_Restaurant': "ភោជនីយដ្ឋាន", 'cat_Airport': "ព្រលានយន្តហោះ", 'check': "ពិនិត្យ", 'nativeLabel': "ភាសាកំណើត", 'selectStep': "1. ជ្រើសរើសស្ថានភាព", 'speakStep': "2. ការអនុវត្តនិយាយ", 'title': "ជ្រើសរើសស្ថានភាព", 'start': "ចាប់ផ្តើម", 'back': "ត្រឡប់ក្រោយ", 'listening': "កំពុងស្តាប់...", 'placeholder': "និយាយ...", 'msgPerfect': "ល្អណាស់!", 'msgGood': "ល្អ!", 'msgBad': "ព្យាយាមម្តងទៀត", 'correction': "ចម្លើយ:", 'listen': "ស្តាប់", 'why': "ហេតុអ្វី?", 'aiName': "គ្រូ AI",
             'btnFeedback': "ផ្ញើមតិ", 'feedbackTitle': "មតិយោបល់", 'phFeedback': "សរសេរមតិ...", 'phContact': "ឈ្មោះ, ទំនាក់ទំនង (អ៊ីមែល, ទូរស័ព្ទ)", 'btnSend': "ផ្ញើ", 'btnClose': "បិទ", 'msgSent': "បានផ្ញើ។" },
     'si': { 'selectTarget': "ඔබ ඉගෙන ගැනීමට කැමති භාෂාව කුමක්ද?", 'cat_School': "පාසල", 'cat_Travel': "සංචාරය", 'cat_Hospital': "රෝහල", 'cat_Market': "වෙළඳපොළ", 'cat_Restaurant': "ආපනශාලාව", 'cat_Airport': "ගුවන් තොටුපළ", 'check': "පරීක්ෂා කරන්න", 'nativeLabel': "මව් භාෂාව", 'selectStep': "1. අවස්ථාව තෝරන්න", 'speakStep': "2. කතා කිරීමේ පුහුණුව", 'title': "තෝරන්න", 'start': "අරඹන්න", 'back': "ආපසු", 'listening': "සවන් දෙමින්...", 'placeholder': "කතා කරන්න...", 'msgPerfect': "නියමයි!", 'msgGood': "හොඳයි!", 'msgBad': "නැවත උත්සාහ කරන්න", 'correction': "පිළිතුර:", 'listen': "අහන්න", 'why': "ඇයි?", 'aiName': "AI ගුරුවරයා",
             'btnFeedback': "ප්‍රතිචාර යවන්න", 'feedbackTitle': "ප්‍රතිචාර", 'phFeedback': "ඔබේ අදහස් ලියන්න...", 'phContact': "නම, සම්බන්ධතා (ඊමේල්, දුරකථන)", 'btnSend': "යවන්න", 'btnClose': "වසන්න", 'msgSent': "යැව්වා." },
     'my': { 'selectTarget': "ဘယ်ဘာသာစကားကို သင်ချင်ပါသလဲ။", 'cat_School': "ကျောင်း", 'cat_Travel': "ခရီးသွား", 'cat_Hospital': "ဆေးရုံ", 'cat_Market': "ဈေး", 'cat_Restaurant': "စားသောက်ဆိုင်", 'cat_Airport': "လေဆိပ်", 'check': "စစ်ဆေးပါ", 'nativeLabel': "မိခင်ဘာသာစကား", 'selectStep': "1. အခြေအနေရွေးပါ", 'speakStep': "2. စကားပြောလေ့ကျင့်ပါ", 'title': "ရွေးချယ်ပါ", 'start': "စတင်ပါ", 'back': "နောက်သို့", 'listening': "နားထောင်နေသည်...", 'placeholder': "ပြောပါ...", 'msgPerfect': "ကောင်းပါတယ်!", 'msgGood': "ကောင်းတယ်!", 'msgBad': "ပြန်ကြိုးစားပါ", 'correction': "အဖြေ:", 'listen': "နားထောင်ရန်", 'why': "ဘာကြောင့်လဲ?", 'aiName': "AI ဆရာ",
             'btnFeedback': "အကြံပြုချက်ပေးပို့ရန်", 'feedbackTitle': "အကြံပြုချက်", 'phFeedback': "အကြံပြုချက်ရေးပါ...", 'phContact': "အမည်၊ ဆက်သွယ်ရန် (အီးမေးလ်၊ ဖုန်း)", 'btnSend': "ပို့မည်", 'btnClose': "ပိတ်မည်", 'msgSent': "ပို့လိုက်ပြီ။" },
     'bn': { 'selectTarget': "আপনি কোন ভাষা শিখতে চান?", 'cat_School': "স্কুল", 'cat_Travel': "ভ্রমণ", 'cat_Hospital': "হাসপাতাল", 'cat_Market': "বাজার", 'cat_Restaurant': "রেস্তোরাঁ", 'cat_Airport': "বিমানবন্দর", 'check': "যাচাই করুন", 'nativeLabel': "মাতৃভাষা", 'selectStep': "1. পরিস্থিতি নির্বাচন করুন", 'speakStep': "2. কথা বলার অনুশীলন", 'title': "নির্বাচন করুন", 'start': "শুরু করুন", 'back': "ফিরে যান", 'listening': "শুনছি...", 'placeholder': "বলুন...", 'msgPerfect': "চমৎকার!", 'msgGood': "ভালো!", 'msgBad': "আবার চেষ্টা করুন", 'correction': "উত্তর:", 'listen': "শুনুন", 'why': "কেন?", 'aiName': "AI শিক্ষক",
             'btnFeedback': "মতামত পাঠান", 'feedbackTitle': "মতামত", 'phFeedback': "আপনার মতামত লিখুন...", 'phContact': "নাম, যোগাযোগ (ইমেল, ফোন)", 'btnSend': "পাঠান", 'btnClose': "বন্ধ করুন", 'msgSent': "পাঠানো হয়েছে।" },
     'lo': { 'selectTarget': "ເຈົ້າຢາກຮຽນພາສາຫຍັງ?", 'cat_School': "ໂຮງຮຽນ", 'cat_Travel': "ການທ່ອງທ່ຽວ", 'cat_Hospital': "ໂຮງໝໍ", 'cat_Market': "ຕະຫຼາດ", 'cat_Restaurant': "ຮ້ານອາຫານ", 'cat_Airport': "ສະໜາມບິນ", 'check': "ກວດເບິ່ງ", 'nativeLabel': "ພາສາແມ່", 'selectStep': "1. ເລືອກສະຖານະການ", 'speakStep': "2. ຝຶກເວົ້າ", 'title': "ເລືອກ", 'start': "ເລີ່ມຕົ້ນ", 'back': "ກັບຄືນ", 'listening': "ກຳລັງຟັງ...", 'placeholder': "ເວົ້າ...", 'msgPerfect': "ດີຫຼາຍ!", 'msgGood': "ດີ!", 'msgBad': "ລອງໃໝ່", 'correction': "ຄຳຕອບ:", 'listen': "ຟັງ", 'why': "ຍ້ອນຫຍັງ?", 'aiName': "ຄູ AI",
             'btnFeedback': "ສົ່ງຄວາມຄິດເຫັນ", 'feedbackTitle': "ຄວາມຄິດເຫັນ", 'phFeedback': "ຂຽນຄວາມຄິດເຫັນ...", 'phContact': "ຊື່, ຕິດຕໍ່ (ອີເມວ, ໂທລະສັບ)", 'btnSend': "ສົ່ງ", 'btnClose': "ປິດ", 'msgSent': "ສົ່ງແລ້ວ." }
}

# Questions - Initialize
QUESTIONS = [
    # --- SCHOOL (10 Questions) ---
    {
        "cat":"School", "ko":"선생님, 질문 있어요.", "en":"Teacher, I have a question.", 
        "vn":"Thưa thầy, em có câu hỏi.", "cn":"老师，我有一个问题。", "th":"คุณครูคะ มีคำถามค่ะ", "ph":"Guro, may tanong ako.", "id":"Guru, saya ada pertanyaan.", "jp":"先生、質問があります。",
        "mn":"Багшаа, надад асуулт байна.", "uz":"Ustoz, menda savol bor.", "ne":"शिक्षक, मसँग एउटा प्रश्न छ।", "km":"លោកគ្រូ ខ្ញុំមានសំណួរ។", "si":"ගුරුතුමනි, මට ප්‍රශ්නයක් තිබේ.", "my":"ဆရာ၊ ကျွန်တော့်မှာ မေးခွန်းတစ်ခုရှိတယ်။", "bn":"শিক্ষক, আমার একটি প্রশ্ন আছে।", "lo":"ຄູອາຈານ, ຂ້ອຍມີຄຳຖາມ.", "ru":"Учитель, у меня есть вопрос.", "kz":"Мұғалім, менде сұрақ бар."
    },
    {
        "cat":"School", "ko":"다시 한번 설명해 주세요.", "en":"Please explain it again.", 
        "vn":"Xin giải thích lại lần nữa.", "cn":"请再解释一遍。", "th":"ช่วยอธิบายอีกครั้งได้ไหมคะ", "ph":"Paki-paliwanag ulit.", "id":"Tolong jelaskan lagi.", "jp":"もう一度説明してください。",
        "mn":"Дахин тайлбарлаж өгнө үү.", "uz":"Iltimos, qaytadan tushuntirib bering.", "ne":"कृपया फेरि व्याख्या गर्नुहोस्।", "km":"សូមពន្យល់ម្តងទៀត។", "si":"කරුණාකර එය නැවත පැහැදිලි කරන්න.", "my":"ကျေးဇူးပြုပြီး ပြန်ရှင်းပြပေးပါ။", "bn":"দয়া করে আবার ব্যাখ্যা করুন।", "lo":"ກະລຸນາອະທິບາຍອີກເທື່ອໜຶ່ງ.", "ru":"Пожалуйста, объясните еще раз.", "kz":"Қайта түсіндіріп беріңізші."
    },
    {
        "cat":"School", "ko":"화장실 다녀와도 될까요?", "en":"May I go to the bathroom?", 
        "vn":"Em có thể đi vệ sinh được không?", "cn":"我可以去洗手间吗？", "th":"ขออนุญาตไปห้องน้ำได้ไหมคะ", "ph":"Pwede ba akong pumunta sa banyo?", "id":"Bolehkah saya ke toilet?", "jp":"トイレに行ってもいいですか？",
        "mn":"Би бие засаад ирж болох уу?", "uz":"Hojatxonaga borib kelsam maylimi?", "ne":"के म शौचालय जान सक्छु?", "km":"តើខ្ញុំអាចទៅបន្ទប់ទឹកបានទេ?", "si":"මට වැසිකිළියට යන්න පුළුවන්ද?", "my":"အိမ်သာသွားလို့ရမလား။", "bn":"আমি কি বাথরুমে যেতে পারি?", "lo":"ຂ້ອຍຂໍໄປຫ້ອງນຳ້ໄດ້ບໍ່?", "ru":"Можно выйти в туалет?", "kz":"Дәретханаға барып келуге бола ма?"
    },
    {
        "cat":"School", "ko":"한국어를 배우고 싶어요.", "en":"I want to learn Korean.", 
        "vn":"Tôi muốn học tiếng Hàn.", "cn":"我想学韩语。", "th":"ฉันอยากเรียนภาษาเกาหลี", "ph":"Gusto kong matuto ng Korean.", "id":"Saya ingin belajar bahasa Korea.", "jp":"韓国語を習いたいです。",
        "mn":"Би Солонгос хэл сурмаар байна.", "uz":"Men koreys tilini o'rganmoqchiman.", "ne":"म कोरियन भाषा सिक्न चाहन्छु।", "km":"ខ្ញុំចង់រៀនភាសាកូរ៉េ។", "si":"මට කොරියානු භාෂාව ඉගෙන ගැනීමට අවශ්‍යයි.", "my":"ကျွန်တော် ကိုရီးယားစကား သင်ချင်ပါတယ်။", "bn":"আমি কোরিয়ান ভাষা শিখতে চাই।", "lo":"ຂ້ອຍຢາກຮຽນພາສາເກົາຫຼີ.", "ru":"Я хочу выучить корейский.", "kz":"Мен корей тілін үйренгім келеді."
    },
    {
        "cat":"School", "ko":"천천히 말해 주세요.", "en":"Please speak slowly.", 
        "vn":"Xin hãy nói chậm lại.", "cn":"请慢一点说。", "th":"ช่วยพูดช้าๆ หน่อยได้ไหมคะ", "ph":"Pakibagalan ang pagsasalita.", "id":"Tolong bicara pelan-pelan.", "jp":"ゆっくり話してください。",
        "mn":"Удаан ярина уу.", "uz":"Iltimos, sekinroq gapiring.", "ne":"कृपया बिस्तारै बोल्नुहोस्।", "km":"សូមនិយាយយឺតៗ។", "si":"කරුණාකර සෙමින් කතා කරන්න.", "my":"ကျေးဇူးပြုပြီး ဖြည်းဖြည်းပြောပါ။", "bn":"দয়া করে ধীরে বলুন।", "lo":"ກະລຸນາເວົ້າຊ້າໆ.", "ru":"Говорите медленнее, пожалуйста.", "kz":"Баяу сөйлеңізші."
    },
    {
        "cat":"School", "ko":"숙제를 잊어버렸어요.", "en":"I forgot my homework.", 
        "vn":"Em quên làm bài tập rồi.", "cn":"我忘记带作业了。", "th":"ฉันลืมทำการบ้าน", "ph":"Nakalimutan ko ang assignment ko.", "id":"Saya lupa PR saya.", "jp":"宿題を忘れました。",
        "mn":"Би даалгавраа мартчихсан.", "uz":"Men uy vazifamni unutibman.", "ne":"मैले गृहकार्य बिर्सें।", "km":"ខ្ញុំភ្លេចធ្វើកិច្ចការផ្ទះ។", "si":"මට ගෙදර වැඩ අමතක වුණා.", "my":"အိမ်စာမေ့သွားတယ်။", "bn":"আমি আমার বাড়ির কাজ ভুলে গেছি।", "lo":"ຂ້ອຍລືມວຽກບ້ານ.", "ru":"Я забыл домашнее задание.", "kz":"Мен үй тапсырмасын ұмытып кеттім."
    },
    {
        "cat":"School", "ko":"연필 좀 빌려주세요.", "en":"Can I borrow a pencil?", 
        "vn":"Cho mình mượn bút chì với.", "cn":"能借我一支铅笔吗？", "th":"ขอยืมดินสอหน่อยได้ไหมคะ", "ph":"Pwede bang humiram ng lapis?", "id":"Bolehkah saya pinjam pensil?", "jp":"鉛筆を借りてもいいですか？",
        "mn":"Надад харандаа зээлээч.", "uz":"Qalam berib tura olasizmi?", "ne":"के म पेन्सिल लिन सक्छु?", "km":"តើខ្ញុំអាចខ្ចីខ្មៅដៃបានទេ?", "si":"මට පැන්සලක් ණයට ගත හැකිද?", "my":"ခဲတံငှားလို့ရမလား။", "bn":"আমি কি একটি পেন্সিল ধার করতে পারি?", "lo":"ຂ້ອຍຂໍຢືມສໍຂາວໄດ້ບໍ່?", "ru":"Можно одолжить карандаш?", "kz":"Қалам сұрап тұра аламын ба?"
    },
    {
        "cat":"School", "ko":"시험이 언제예요?", "en":"When is the exam?", 
        "vn":"Khi nào thi vậy?", "cn":"什么时候考试？", "th":"สอบเมื่อไหร่คะ", "ph":"Kailan ang exam?", "id":"Kapan ujiannya?", "jp":"試験はいつですか？",
        "mn":"Шалгалт хэзээ вэ?", "uz":"Imtihon qachon?", "ne":"परीक्षा कहिले हो?", "km":"តើការប្រឡងនៅពេលណា?", "si":"විභාගය කවද්ද?", "my":"စာမေးပွဲ ဘယ်တော့လဲ။", "bn":"পরীক্ষা কবে?", "lo":"ການສອບເສັງແມ່ນເມື່ອໃດ?", "ru":"Когда экзамен?", "kz":"Емтихан қашан?"
    },
    {
        "cat":"School", "ko":"감사합니다, 선생님.", "en":"Thank you, Teacher.", 
        "vn":"Em cảm ơn thầy/cô.", "cn":"谢谢老师。", "th":"ขอบคุณค่ะ คุณครู", "ph":"Salamat po, Guro.", "id":"Terima kasih, Guru.", "jp":"ありがとうございます、先生。",
        "mn":"Баярлалаа, багшаа.", "uz":"Rahmat, ustoz.", "ne":"धन्यवाद, शिक्षक।", "km":"សូមអរគុណលោកគ្រូ។", "si":"ස්තූතියි ගුරුතුමනි.", "my":"ကျေးဇူးတင်ပါတယ် ဆရာ။", "bn":"ধন্যবাদ, শিক্ষক।", "lo":"ຂອບໃຈ, ຄູອາຈານ.", "ru":"Спасибо, учитель.", "kz":"Рахмет, мұғалім."
    },
    {
        "cat":"School", "ko":"무슨 뜻이에요?", "en":"What does it mean?", 
        "vn":"Nó có nghĩa là gì?", "cn":"这是什么意思？", "th":"หมายความว่าอย่างไรคะ", "ph":"Anong ibig sabihin nito?", "id":"Apa artinya?", "jp":"どういう意味ですか？",
        "mn":"Энэ ямар утгатай вэ?", "uz":"Bu nimani anglatadi?", "ne":"यसको अर्थ के हो?", "km":"តើវាមានន័យយ៉ាងណា?", "si":"එහි තේරුම කුමක්ද?", "my":"ဒါဘာအဓိပ္ပါယ်လဲ။", "bn":"এর মানে কি?", "lo":"ມັນໝາຍຄວາມວ່າແນວໃດ?", "ru":"Что это значит?", "kz":"Бұл нені білдіреді?"
    }
]

QUESTIONS.extend([
    # --- TRAVEL (10 Questions) ---
    {
        "cat":"Travel", "ko":"예약 확인해 주세요.", "en":"I have a reservation.", 
        "vn":"Tôi đã đặt trước.", "cn":"我有预订。", "th":"ฉันจองไว้แล้วค่ะ", "ph":"May reservation ako.", "id":"Saya sudah reservasi.", "jp":"予約しています。",
        "mn":"Захиалгаа баталгаажуулна уу.", "uz":"Bandligimni tekshirib bering.", "ne":"मेरो बुकिङ पक्का गर्नुहोस्।", "km":"សូមពិនិត្យការកក់។", "si":"මගේ වෙන්කරවා ගැනීම තහවුරු කරන්න.", "my":"ဘွတ်ကင်အတည်ပြုပေးပါ။", "bn":"আমার রিজার্ভেশন নিশ্চিত করুন।", "lo":"ຢືນຢັນການຈອງໃຫ້ແດ່.", "ru":"У меня есть бронь.", "kz":"Брондауды растаңызшы."
    },
    {
        "cat":"Travel", "ko":"빈 방 있나요?", "en":"Do you have a vacant room?", 
        "vn":"Có phòng trống không?", "cn":"有空房吗？", "th":"มีห้องว่างไหมคะ", "ph":"May bakanteng kwarto ba?", "id":"Ada kamar kosong?", "jp":"空き部屋はありますか？",
        "mn":"Сул өрөө байна уу?", "uz":"Bo'sh xona bormi?", "ne":"के त्यहाँ खाली कोठा छ?", "km":"តើមានបន្ទប់ទំនេរទេ?", "si":"හිස් කාමරයක් තිබේද?", "my":"အခန်းလွတ်ရှိလား။", "bn":"খালি রুম আছে কি?", "lo":"ມີຫ້ອງຫວ່າງບໍ່?", "ru":"У вас есть свободный номер?", "kz":"Бос бөлме бар ма?"
    },
    {
        "cat":"Travel", "ko":"와이파이 비밀번호가 뭐예요?", "en":"What is the WiFi password?", 
        "vn":"Mật khẩu WiFi là gì?", "cn":"WiFi密码是多少？", "th":"รหัสผ่าน WiFi คืออะไรคะ", "ph":"Ano ang password ng WiFi?", "id":"Apa password WiFi-nya?", "jp":"Wi-Fiのパスワードは何ですか？",
        "mn":"WiFi нууц үг юу вэ?", "uz":"Wi-Fi paroli nima?", "ne":"WiFi पासवर्ड के हो?", "km":"តើលេខសម្ងាត់ WiFi គឺជាអ្វី?", "si":"WiFi මුරපදය කුමක්ද?", "my":"WiFi စကားဝှက်က ဘာလဲ။", "bn":"ওয়াইফাই পাসওয়ার্ড কি?", "lo":"ລະຫັດ WiFi ແມ່ນຫຍັງ?", "ru":"Какой пароль от Wi-Fi?", "kz":"WiFi құпия сөзі қандай?"
    },
    {
        "cat":"Travel", "ko":"택시를 불러주세요.", "en":"Please call a taxi.", 
        "vn":"Làm ơn gọi giúp tôi taxi.", "cn":"请帮我叫辆出租车。", "th":"ช่วยเรียกแท็กซี่ให้หน่อยค่ะ", "ph":"Pakitawag ng taxi.", "id":"Tolong panggilkan taksi.", "jp":"タクシーを呼んでください。",
        "mn":"Такси дуудаад өгөөч.", "uz":"Iltimos, taksi chaqirib bering.", "ne":"कृपया ट्याक्सी बोलाउनुहोस्।", "km":"សូមហៅតាក់ស៊ីឱ្យខ្ញុំផង។", "si":"කරුණාකර ටැක්සියක් අමතන්න.", "my":"တက္ကစီခေါ်ပေးပါ။", "bn":"দয়া করে একটি ট্যাক্সি ডাকুন।", "lo":"ເອີ້ນແທັກຊີໃຫ້ແດ່.", "ru":"Пожалуйста, вызовите такси.", "kz":"Такси шақырып беріңізші."
    },
    {
        "cat":"Travel", "ko":"지하철역이 어디예요?", "en":"Where is the subway station?", 
        "vn":"Ga tàu điện ngầm ở đâu?", "cn":"地铁站在哪里？", "th":"สถานีรถไฟใต้ดินอยู่ที่ไหนคะ", "ph":"Saan ang istasyon ng subway?", "id":"Di mana stasiun metro?", "jp":"地下鉄の駅はどこですか？",
        "mn":"Метроны буудал хаана вэ?", "uz":"Metro bekati qayerda?", "ne":"सबवे स्टेशन कहाँ छ?", "km":"តើស្ថានីយ៍រថភ្លើងក្រោមដីនៅឯណា?", "si":"උමං දුම්රිය ස්ථානය කොහෙද?", "my":"မြေအောက်ရထားဘူတာ ဘယ်မှာလဲ။", "bn":"সাবওয়ে স্টেশন কোথায়?", "lo":"ສະຖານີລົດໄຟໃຕ້ດິນຢູ່ໃສ?", "ru":"Где станция метро?", "kz":"Метро станциясы қайда?"
    },
    {
        "cat":"Travel", "ko":"이 주소로 가주세요.", "en":"Take me to this address.", 
        "vn":"Đưa tôi đến địa chỉ này.", "cn":"请带我去这个地址。", "th":"ไปส่งที่ที่อยู่นี้หน่อยค่ะ", "ph":"Dalhin mo ako sa address na ito.", "id":"Antar saya ke alamat ini.", "jp":"この住所へ行ってください。",
        "mn":"Энэ хаяг руу явмаар байна.", "uz":"Meni shu manzilga olib boring.", "ne":"मलाई यो ठेगानामा लैजानुहोस्।", "km":"សូមជូនខ្ញុំទៅអាសយដ្ឋាននេះ។", "si":"මාව මෙම ලිපිනයට රැගෙන යන්න.", "my":"ဒီလိပ်စာကို ပို့ပေးပါ။", "bn":"আমাকে এই ঠিকানায় নিয়ে যান।", "lo":"ໄປທີ່ຢູ່ບ່ອນນີ້ແດ່.", "ru":"Пожалуйста, отвезите меня по этому адресу.", "kz":"Осы мекенжайға апарыңызшы."
    },
    {
        "cat":"Travel", "ko":"얼마나 걸려요?", "en":"How long does it take?", 
        "vn":"Mất bao lâu?", "cn":"需要多长时间？", "th":"ใช้เวลานานเท่าไหร่คะ", "ph":"Gaano katagal?", "id":"Berapa lama?", "jp":"どのくらいかかりますか？",
        "mn":"Хэр удах вэ?", "uz":"Qancha vaqt oladi?", "ne":"कति समय लाग्छ?", "km":"តើវាចំណាយពេលប៉ុន្មាន?", "si":"කොපමණ කාලයක් ගතවේද?", "my":"ဘယ်လောက်ကြာမလဲ။", "bn":"কতক্ষণ লাগবে?", "lo":"ໃຊ້ເວລາເທົ່າໃດ?", "ru":"Сколько времени это займет?", "kz":"Қанша уақыт алады?"
    },
    {
        "cat":"Travel", "ko":"사진 좀 찍어주세요.", "en":"Please take a picture of me.", 
        "vn":"Chụp giúp tôi tấm ảnh với.", "cn":"请帮我拍张照。", "th":"ช่วยถ่ายรูปให้หน่อยได้ไหมคะ", "ph":"Pwede bang pa-picture?", "id":"Tolong ambilkan foto.", "jp":"写真を撮ってください。",
        "mn":"Зураг дараад өгч болох уу.", "uz":"Rasmga olib qo'ya olasizmi?", "ne":"कृपया मेरो तस्बिर खिच्नुहोस्।", "km":"សូមថតរូបឱ្យខ្ញុំផង។", "si":"කරුණාකර මගේ ඡායාරූපයක් ගන්න.", "my":"ဓာတ်ပုံရိုက်ပေးလို့ရမလား။", "bn":"দয়া করে আমার একটি ছবি তুলুন।", "lo":"ຖ່າຍຮູບໃຫ້ແດ່.", "ru":"Сфотографируйте меня, пожалуйста.", "kz":"Суретке түсіріп бересіз бе?"
    },
    {
        "cat":"Travel", "ko":"여기가 정말 아름다워요.", "en":"It is beautiful here.", 
        "vn":"Ở đây đẹp quá.", "cn":"这里真漂亮。", "th":"ที่นี่สวยมากค่ะ", "ph":"Ang ganda dito.", "id":"Di sini indah sekali.", "jp":"ここは本当に美しいです。",
        "mn":"Энд үнэхээр үзэсгэлэнтэй юм.", "uz":"Bu yer juda chiroyli.", "ne":"यहाँ धेरै सुन्दर छ।", "km":"ទីនេះស្អាតណាស់។", "si":"මෙහි ලස්සනයි.", "my":"ဒီနေရာက အရမ်းလှတယ်။", "bn":"এখানে খুব সুন্দর।", "lo":"ບ່ອນນີ້ງາມຫຼາຍ.", "ru":"Здесь очень красиво.", "kz":"Бұл жер өте әдемі."
    },
    {
        "cat":"Travel", "ko":"지도 좀 얻을 수 있을까요?", "en":"Can I get a map?", 
        "vn":"Cho tôi xin bản đồ được không?", "cn":"能给我一份地图吗？", "th":"ขอแผนที่หน่อยได้ไหมคะ", "ph":"Pwede bang makahingi ng mapa?", "id":"Bisa minta peta?", "jp":"地図をもらえますか？",
        "mn":"Би газрын зураг авч болох уу?", "uz":"Xarita olsam bo'ladimi?", "ne":"के म नक्सा पाउन सक्छु?", "km":"តើខ្ញុំអាចសុំផែនទីបានទេ?", "si":"මට සිතියමක් ලබා ගත හැකිද?", "my":"မြေပုံရနိုင်မလား။", "bn":"আমি কি একটি মানচিত্র পেতে পারি?", "lo":"ຂໍແຜນທີ່ໄດ້ບໍ່?", "ru":"Можно мне карту?", "kz":"Карта алуға бола ма?"
    }
])

QUESTIONS.extend([
    # --- HOSPITAL (10 Questions) ---
    {
        "cat":"Hospital", "ko":"머리가 아파요.", "en":"I have a headache.", 
        "vn":"Tôi bị đau đầu.", "cn":"我头痛。", "th":"ฉันปวดหัวค่ะ", "ph":"Masakit ang ulo ko.", "id":"Saya sakit kepala.", "jp":"頭が痛いです。",
        "mn":"Толгой өвдөж байна.", "uz":"Boshim og'riyapti.", "ne":"मेरो टाउको दुखेको छ।", "km":"ខ្ញុំឈឺក្បាល។", "si":"මට හිසරදයක් තියෙනවා.", "my":"ခေါင်းကိုက်တယ်။", "bn":"আমার মাথা ব্যথা করছে।", "lo":"ຂ້ອຍເຈັບຫົວ.", "ru":"У меня болит голова.", "kz":"Басым ауырып тұр."
    },
    {
        "cat":"Hospital", "ko":"열이 나요.", "en":"I have a fever.", 
        "vn":"Tôi bị sốt.", "cn":"我发烧了。", "th":"ฉันมีไข้ค่ะ", "ph":"May lagnat ako.", "id":"Saya demam.", "jp":"熱があります。",
        "mn":"Би халуурч байна.", "uz":"Isitmam bor.", "ne":"मलाई ज्वरो आएको छ।", "km":"ខ្ញុំក្តៅខ្លួន។", "si":"මට උණ.", "my":"ကိုယ်ပူနေတယ်။", "bn":"আমার জ্বর হয়েছে।", "lo":"ຂ້ອຍເປັນໄຂ້.", "ru":"У меня температура.", "kz":"Менің қызуым көтеріліп тұр."
    },
    {
        "cat":"Hospital", "ko":"배가 너무 아파요.", "en":"My stomach hurts so much.", 
        "vn":"Bụng tôi đau quá.", "cn":"也就是肚子疼。", "th":"ปวดท้องมากค่ะ", "ph":"Masakit ang tiyan ko.", "id":"Perut saya sakit sekali.", "jp":"お腹がとても痛いです。",
        "mn":"Миний гэдэс маш их өвдөж байна.", "uz":"Qornim juda og'riyapti.", "ne":"मेरो पेट धेरै दुख्छ।", "km":"ខ្ញុំឈឺពោះខ្លាំងណាស់។", "si":"මගේ බඩ ගොඩක් රිදෙනවා.", "my":"ဗိုက်အရမ်းနာတယ်။", "bn":"আমার পেট খুব ব্যথা করছে।", "lo":"ທ້ອງຂ້ອຍເຈັບຫຼາຍ.", "ru":"У меня сильно болит живот.", "kz":"Ішім қатты ауырып тұр."
    },
    {
        "cat":"Hospital", "ko":"응급실로 가주세요.", "en":"Please go to the ER.", 
        "vn":"Làm ơn đến phòng cấp cứu.", "cn":"请去急诊室。", "th":"โปรดไปห้องฉุกเฉิน", "ph":"Dalhin mo ako sa ER.", "id":"Tolong ke UGD.", "jp":"救急室へ行ってください。",
        "mn":"Түргэн тусламж руу явна уу.", "uz":"Tez yordam bo'limiga olib boring.", "ne":"कृपया आकस्मिक कक्षमा जानुहोस्।", "km":"សូមទៅកាន់បន្ទប់សង្គ្រោះបន្ទាន់។", "si":"කරුණාකර හදිසි ප්‍රතිකාර ඒකකයට යන්න.", "my":"အရေးပေါ်ခန်းကို သွားပေးပါ။", "bn":"দয়া করে জরুরি বিভাগে যান।", "lo":"ໄປຫ້ອງສຸກເສີນແດ່.", "ru":"Пожалуйста, в отделение скорой помощи.", "kz":"Жедел жәрдем бөліміне апарыңызшы."
    },
    {
        "cat":"Hospital", "ko":"일주일 동안 아팠어요.", "en":"I've been sick for a week.", 
        "vn":"Tôi ốm một tuần nay rồi.", "cn":"我病了一周了。", "th":"ฉันป่วยมาอาทิตย์นึงแล้ว", "ph":"Isang linggo na akong may sakit.", "id":"Saya sudah sakit seminggu.", "jp":"一週間ずっと具合が悪いです。",
        "mn":"Би долоо хоног өвдсөн.", "uz":"Bir haftadan beri kasalman.", "ne":"म एक हप्तादेखि बिरामी छु।", "km":"ខ្ញុំឈឺមួយសប្តាហ៍ហើយ។", "si":"මම සතියක් තිස්සේ අසනීපෙන්.", "my":"နေမကောင်းဖြစ်တာ တစ်ပတ်ရှိပြီ။", "bn":"আমি এক সপ্তাহ ধরে অসুস্থ।", "lo":"ຂ້ອຍບໍ່ສະບາຍມາອາທິດໜຶ່ງແລ້ວ.", "ru":"Я болею уже неделю.", "kz":"Бір апта бойы ауырып жүрмін."
    },
    {
        "cat":"Hospital", "ko":"약국이 어디에 있나요?", "en":"Where is the pharmacy?", 
        "vn":"Nhà thuốc ở đâu?", "cn":"药店在哪里？", "th":"ร้านขายยาอยู่ที่ไหนคะ", "ph":"Saan ang botika?", "id":"Di mana apotek?", "jp":"薬局はどこですか？",
        "mn":"Эмийн сан хаана вэ?", "uz":"Dorixona qayerda?", "ne":"औषधि पसल कहाँ छ?", "km":"តើឱសថស្ថាននៅឯណា?", "si":"ෆාමසිය කොහෙද?", "my":"ဆေးဆိုင် ဘယ်မှာလဲ။", "bn":"ফার্মেসী কোথায়?", "lo":"ຮ້ານຂາຍຢາຢູ່ໃສ?", "ru":"Где аптека?", "kz":"Дәріхана қайда?"
    },
    {
        "cat":"Hospital", "ko":"도와주세요!", "en":"Help me!", 
        "vn":"Cứu tôi với!", "cn":"救命！", "th":"ช่วยด้วย!", "ph":"Tulong!", "id":"Tolong!", "jp":"助けてください！",
        "mn":"Туслаарай!", "uz":"Yordam bering!", "ne":"मलाई मद्दत गर्नुहोस्!", "km":"ជួយខ្ញុំផង!", "si":"මට උදව් කරන්න!", "my":"ကယ်ပါ!", "bn":"আমাকে সাহায্য করুন!", "lo":"ຊ່ວຍແດ່!", "ru":"Помогите!", "kz":"Көмектесіңіз!"
    },
    {
        "cat":"Hospital", "ko":"감기에 걸렸어요.", "en":"I caught a cold.", 
        "vn":"Tôi bị cảm rồi.", "cn":"我感冒了。", "th":"ฉันเป็นหวัด", "ph":"May sipon ako.", "id":"Saya masuk angin.", "jp":"風邪をひきました。",
        "mn":"Би ханиад хүрсэн.", "uz":"Shamollab qoldim.", "ne":"मलाई रुघा लाग्यो।", "km":"ខ្ញុំផ្តាសាយ។", "si":"මට සෙම්ප්‍රතිශ්‍යාව වැළඳී ඇත.", "my":"အအေးမိသွားတယ်။", "bn":"আমার ঠান্ডা লেগেছে।", "lo":"ຂ້ອຍເປັນຫວັດ.", "ru":"Я простудился.", "kz":"Тұмау тиіп қалды."
    },
    {
        "cat":"Hospital", "ko":"여기가 부러진 것 같아요.", "en":"I think it's broken.", 
        "vn":"Hình như bị gãy rồi.", "cn":"我想这里骨折了。", "th":"ฉันคิดว่ามันหัก", "ph":"Sa tingin ko bali ito.", "id":"Sepertinya patah.", "jp":"骨折したみたいです。",
        "mn":"Энд хугарсан юм шиг байна.", "uz":"Menimcha, bu singan.", "ne":"मलाई लाग्छ यो भाँचिएको छ।", "km":"ខ្ញុំគិតថាវាបាក់។", "si":"මම හිතන්නේ එය කැඩී ඇති බවයි.", "my":"ကျိုးသွားတယ် ထင်တယ်။", "bn":"আমার মনে হয় এটা ভেঙে গেছে।", "lo":"ຂ້ອຍຄິດວ່າມັນຫັກ.", "ru":"Кажется, сломано.", "kz":"Сынған сияқты."
    },
    {
        "cat":"Hospital", "ko":"의사 선생님을 보고 싶어요.", "en":"I want to see a doctor.", 
        "vn":"Tôi muốn gặp bác sĩ.", "cn":"我想看医生。", "th":"ฉันอยากพบหมอ", "ph":"Gusto kong makita ang doktor.", "id":"Saya ingin bertemu dokter.", "jp":"医者に診てもらいたいです。",
        "mn":"Би эмчид үзүүлмээр байна.", "uz":"Men shifokorni ko'rmoqchiman.", "ne":"म डाक्टरलाई देखाउन चाहन्छु।", "km":"ខ្ញុំចង់ជួបគ្រូពេទ្យ។", "si":"මට වෛද්‍යවරයකු හමුවීමට අවශ්‍යයි.", "my":"ဆရာဝန်နဲ့ ပြချင်ပါတယ်။", "bn":"আমি একজন ডাক্তার দেখাতে চাই।", "lo":"ຂ້ອຍຢາກພົບທ່ານໝໍ.", "ru":"Я хочу к врачу.", "kz":"Дәрігерге қаралғым келеді."
    }
])

QUESTIONS.extend([
    # --- MARKET (10 Questions) ---
    {
        "cat":"Market", "ko":"이거 얼마예요?", "en":"How much is this?", 
        "vn":"Cái này bao nhiêu tiền?", "cn":"这个多少钱？", "th":"อันนี้ราคาเท่าไหร่คะ", "ph":"Magkano ito?", "id":"Berapa harganya?", "jp":"これはいくらですか？",
        "mn":"Энэ ямар үнэтэй вэ?", "uz":"Bu qancha turadi?", "ne":"यसको कति पर्छ?", "km":"តើនេះតម្លៃប៉ុន្មាន?", "si":"මෙය කීයද?", "my":"ဒါဘယ်လောက်လဲ။", "bn":"এটার দাম কত?", "lo":"ອັນນີ້ລາຄາເທົ່າໃດ?", "ru":"Сколько это стоит?", "kz":"Бұл қанша тұрады?"
    },
    {
        "cat":"Market", "ko":"너무 비싸요.", "en":"It's too expensive.", 
        "vn":"Đắt quá.", "cn":"太贵了。", "th":"แพงเกินไปค่ะ", "ph":"Ang mahal naman.", "id":"Terlalu mahal.", "jp":"高すぎます。",
        "mn":"Хэтэрхий үнэтэй байна.", "uz":"Juda qimmat.", "ne":"यो धेरै महँगो छ।", "km":"ថ្លៃ​ពេក។", "si":"එය ඉතා මිල අධිකයි.", "my":"ဈေးကြီးလွန်းတယ်။", "bn":"এটা খুব দামী।", "lo":"ມັນແພງໂພດ.", "ru":"Это слишком дорого.", "kz":"Бұл тым қымбат."
    },
    {
        "cat":"Market", "ko":"깎아주세요.", "en":"Please give me a discount.", 
        "vn":"Giảm giá cho tôi đi.", "cn":"请便宜一点。", "th":"ลดหน่อยได้ไหมคะ", "ph":"Pwede bang tumawad?", "id":"Bisa kurang?", "jp":"まけてください。",
        "mn":"Хямдруулж өгөөч.", "uz":"Arzonroq qilib bering.", "ne":"कृपया मलाई छुट दिनुहोस्।", "km":"សូមបញ្ចុះតម្លៃឱ្យខ្ញុំ។", "si":"කරුණාකර මට වට්ටමක් දෙන්න.", "my":"လျှော့ပေးပါ။", "bn":"দয়া করে আমাকে ডিসকাউন্ট দিন।", "lo":"ຫຼຸດລາຄາໃຫ້ແດ່.", "ru":"Пожалуйста, сделайте скидку.", "kz":"Жеңілдік жасаңызшы."
    },
    {
        "cat":"Market", "ko":"이거 주세요.", "en":"I'll take this one.", 
        "vn":"Tôi lấy cái này.", "cn":"我要这个。", "th":"เอาอันนี้ค่ะ", "ph":"Kukunin ko ito.", "id":"Saya ambil ini.", "jp":"これをください。",
        "mn":"Би үүнийг авъя.", "uz":"Men shuni olaman.", "ne":"म यो लिन्छु।", "km":"ខ្ញុំយកមួយនេះ។", "si":"මම මේක ගන්නවා.", "my":"ဒါယူမယ်။", "bn":"আমি এটা নেব।", "lo":"ຂ້ອຍເອົາອັນນີ້.", "ru":"Я возьму это.", "kz":"Мен осыны аламын."
    },
    {
        "cat":"Market", "ko":"입어봐도 될까요?", "en":"Can I try it on?", 
        "vn":"Tôi mặc thử được không?", "cn":"我可以试穿吗？", "th":"ลองใส่ได้ไหมคะ", "ph":"Pwede bang isukat?", "id":"Boleh saya coba?", "jp":"着てみてもいいですか？",
        "mn":"Би өмсөж үзэж болох уу?", "uz":"Kiyib ko'rsam maylimi?", "ne":"के म यसलाई लगाउन सक्छु?", "km":"តើខ្ញុំអាចសាកល្បងវាបានទេ?", "si":"මට එය ඇඳීමට උත්සාහ කළ හැකිද?", "my":"ဝတ်ကြည့်လို့ရမလား။", "bn":"আমি কি এটা পরে দেখতে পারি?", "lo":"ຂ້ອຍລອງໃສ່ໄດ້ບໍ່?", "ru":"Можно примерить?", "kz":"Киіп көрсем бола ма?"
    },
    {
        "cat":"Market", "ko":"다른 색깔 있나요?", "en":"Do you have another color?", 
        "vn":"Có màu khác không?", "cn":"有别的颜色吗？", "th":"มีสีอื่นไหมคะ", "ph":"May iba pa bang kulay?", "id":"Ada warna lain?", "jp":"他の色はありますか？",
        "mn":"Өөр өнгө байгаа юу?", "uz":"Boshqa rangi bormi?", "ne":"तपाईं सँग अर्को रंग छ?", "km":"តើអ្នកមានពណ៌ផ្សេងទេ?", "si":"ඔබට වෙනත් වර්ණයක් තිබේද?", "my":"တခြားအရောင်ရှိလား။", "bn":"আপনার কি অন্য রঙ আছে?", "lo":"ມີສີອື່ນບໍ່?", "ru":"У вас есть другой цвет?", "kz":"Басқа түсі бар ма?"
    },
    {
        "cat":"Market", "ko":"카드로 계산되나요?", "en":"Can I pay by card?", 
        "vn":"Thanh toán thẻ được không?", "cn":"可以刷卡吗？", "th":"จ่ายบัตรเครดิตได้ไหมคะ", "ph":"Pwede bang mag-credit card?", "id":"Bisa bayar pakai kartu?", "jp":"カードで払えますか？",
        "mn":"Картаар төлж болох уу?", "uz":"Karta orqali to'lasam bo'ladimi?", "ne":"के म कार्डबाट तिर्न सक्छु?", "km":"តើខ្ញុំអាចបង់ប្រាក់តាមកាតបានទេ?", "si":"මට කාඩ්පතෙන් ගෙවිය හැකිද?", "my":"ကတ်နဲ့ပေးလို့ရမလား။", "bn":"আমি কি কার্ড দিয়ে পেমেন্ট করতে পারি?", "lo":"ຈ່າຍບັດໄດ້ບໍ່?", "ru":"Можно оплатить картой?", "kz":"Картамен төлеуге бола ма?"
    },
    {
        "cat":"Market", "ko":"영수증 주세요.", "en":"Please give me a receipt.", 
        "vn":"Cho tôi hóa đơn.", "cn":"请给我收据。", "th":"ขอใบเสร็จด้วยค่ะ", "ph":"Pahingi ng resibo.", "id":"Minta struknya.", "jp":"レシートをください。",
        "mn":"Надад баримт өгөөч.", "uz":"Iltimos, chekni bering.", "ne":"कृपया मलाई रसिद दिनुहोस्।", "km":"សូមឱ្យវិក្កយបត្រមកខ្ញុំ។", "si":"කරුණාකර මට රිසිට්පතක් දෙන්න.", "my":"ဘောက်ချာပေးပါ။", "bn":"দয়া করে আমাকে একটি রসিদ দিন।", "lo":"ຂໍໃບຮັບເງິນແດ່.", "ru":"Пожалуйста, дайте чек.", "kz":"Чек беріңізші."
    },
    {
        "cat":"Market", "ko":"봉투 필요해요.", "en":"I need a bag.", 
        "vn":"Tôi cần túi.", "cn":"我需要袋子。", "th":"ขอถุงด้วยค่ะ", "ph":"Kailangan ko ng bag.", "id":"Saya butuh kantong.", "jp":"袋がいります。",
        "mn":"Надад тор хэрэгтэй.", "uz":"Menga sumka kerak.", "ne":"मलाई झोला चाहिन्छ।", "km":"ខ្ញុំត្រូវការថង់។", "si":"මට බෑගයක් අවශ්‍යයි.", "my":"အိတ်လိုတယ်။", "bn":"আমার একটা ব্যাগ দরকার।", "lo":"ຂ້ອຍຕ້ອງການຖົງ.", "ru":"Мне нужен пакет.", "kz":"Маған пакет керек."
    },
    {
        "cat":"Market", "ko":"환불해 주세요.", "en":"Please refund this.", 
        "vn":"Làm ơn hoàn tiền lại.", "cn":"请退款。", "th":"ขอคืนเงินค่ะ", "ph":"Pakibalik ang bayad.", "id":"Tolong refund.", "jp":"払い戻ししてください。",
        "mn":"Буцаан олголт хийж өгөөч.", "uz":"Iltimos, pulni qaytarib bering.", "ne":"कृपया यो फिर्ता गर्नुहोस्।", "km":"សូមសងប្រាក់វិញ។", "si":"කරුණාකර මෙය ආපසු ගෙවන්න.", "my":"ငွေပြန်အမ်းပေးပါ။", "bn":"দয়া করে এটি ফেরত দিন।", "lo":"ຂໍເງິນຄືນແດ່.", "ru":"Пожалуйста, сделайте возврат.", "kz":"Ақшамды қайтарыңызшы."
    }
])

QUESTIONS.extend([
    # --- RESTAURANT (10 Questions) ---
    {
        "cat":"Restaurant", "ko":"메뉴판 주세요.", "en":"Menu, please.", 
        "vn":"Cho tôi xem menu.", "cn":"请给我菜单。", "th":"ขอเมนูหน่อยค่ะ", "ph":"Penge ng menu.", "id":"Minta menunya.", "jp":"メニューをください。",
        "mn":"Цэс өгөөч.", "uz":"Menyuni bering.", "ne":"कृपया मेनु दिनुहोस्।", "km":"សូមសុំមើលម៉ឺនុយ។", "si":"කරුණාකර මෙනුව දෙන්න.", "my":"မီနူးပေးပါ။", "bn":"দয়া করে মেনু দিন।", "lo":"ຂໍເມນູແດ່.", "ru":"Меню, пожалуйста.", "kz":"Мәзір беріңізші."
    },
    {
        "cat":"Restaurant", "ko":"물 좀 주세요.", "en":"Water, please.", 
        "vn":"Cho tôi xin nước.", "cn":"请给我水。", "th":"ขอน้ำหน่อยค่ะ", "ph":"Penge ng tubig.", "id":"Minta air.", "jp":"お水をください。",
        "mn":"Ус өгөөч.", "uz":"Suv bering.", "ne":"कृपया पानी दिनुहोस्।", "km":"សូមទឹក។", "si":"කරුණාකර වතුර දෙන්න.", "my":"ရေပေးပါ။", "bn":"দয়া করে পানি দিন।", "lo":"ຂໍນຳ້ແດ່.", "ru":"Воды, пожалуйста.", "kz":"Су беріңізші."
    },
    {
        "cat":"Restaurant", "ko":"주문할게요.", "en":"I would like to order.", 
        "vn":"Tôi muốn gọi món.", "cn":"我要点菜。", "th":"สั่งอาหารหน่อยค่ะ", "ph":"Oorder na ako.", "id":"Saya mau pesan.", "jp":"注文します。",
        "mn":"Захиалга өгье.", "uz":"Buyurtma bermoqchiman.", "ne":"म अर्डर गर्न चाहन्छु।", "km":"ខ្ញុំចង់កម្មង់។", "si":"මම ඇණවුම් කිරීමට කැමතියි.", "my":"မှာချင်ပါတယ်။", "bn":"আমি অর্ডার করতে চাই।", "lo":"ຂໍສັ່ງອາຫານ.", "ru":"Я хочу сделать заказ.", "kz":"Тапсырыс бергім келеді."
    },
    {
        "cat":"Restaurant", "ko":"맛있어요?", "en":"Is it delicious?", 
        "vn":"Có ngon không?", "cn":"好吃吗？", "th":"อร่อยไหมคะ", "ph":"Masarap ba?", "id":"Enak?", "jp":"おいしいですか？",
        "mn":"Амттай байна уу?", "uz":"Mazilimi?", "ne":"के यो स्वादिष्ट छ?", "km":"តើវាឆ្ងាញ់ទេ?", "si":"එය රසවත්ද?", "my":"စားကောင်းလား။", "bn":"এটা কি সুস্বাদু?", "lo":"ແຊບບໍ່?", "ru":"Это вкусно?", "kz":"Дәмді ме?"
    },
    {
        "cat":"Restaurant", "ko":"매워요?", "en":"Is it spicy?", 
        "vn":"Có cay không?", "cn":"辣吗？", "th":"เผ็ดไหมคะ", "ph":"Maanghang ba?", "id":"Pedas?", "jp":"辛いですか？",
        "mn":"Халуун ногоотой юу?", "uz":"Achchiqmi?", "ne":"के यो पिरो छ?", "km":"តើវាហឹរទេ?", "si":"එය සැරද?", "my":"စပ်လား။", "bn":"এটা কি ঝাল?", "lo":"ເຜັດບໍ່?", "ru":"Это остро?", "kz":"Ащы ма?"
    },
    {
        "cat":"Restaurant", "ko":"추천해 주세요.", "en":"Please recommend.", 
        "vn":"Giới thiệu giúp tôi.", "cn":"请推荐一下。", "th":"ช่วยแนะนำหน่อยค่ะ", "ph":"Ano ang mare-recommend mo?", "id":"Tolong rekomendasikan.", "jp":"おすすめは何ですか？",
        "mn":"Санал болгооч.", "uz":"Tavsiya qiling.", "ne":"कृपया सिफारिस गर्नुहोस्।", "km":"សូមណែនាំ។", "si":"කරුණාකර නිර්දේශ කරන්න.", "my":"အကြံပြုပေးပါ။", "bn":"দয়া করে সুপারিশ করুন।", "lo":"ແນະນຳແດ່.", "ru":"Порекомендуйте что-нибудь.", "kz":"Ұсыныс жасаңызшы."
    },
    {
        "cat":"Restaurant", "ko":"잘 먹었습니다.", "en":"Thank you for the meal.", 
        "vn":"Cảm ơn vì bữa ăn.", "cn":"我吃饱了。", "th":"อาหารอร่อยมากค่ะ", "ph":"Salamat sa pagkain.", "id":"Terima kasih makanannya.", "jp":"ごちそうさまでした。",
        "mn":"Сайхан хооллолоо.", "uz":"Ovqat uchun rahmat.", "ne":"खानाको लागि धन्यवाद।", "km":"អរគុណសម្រាប់អាហារ។", "si":"කෑමට ස්තූතියි.", "my":"ကျေးဇူးတင်ပါတယ်။", "bn":"খাবারের জন্য ধন্যবাদ।", "lo":"ຂອບໃຈສຳລັບອາຫານ.", "ru":"Спасибо за еду.", "kz":"Тамақ үшін рахмет."
    },
    {
        "cat":"Restaurant", "ko":"계산서 주세요.", "en":"Check, please.", 
        "vn":"Tính tiền nhé.", "cn":"买单。", "th":"เช็คบิลด้วยค่ะ", "ph":"Bill please.", "id":"Minta bill.", "jp":"お会計をお願いします。",
        "mn":"Тооцоогоо хийе.", "uz":"Hisob-kitob qiling.", "ne":"कृपया बिल दिनुहोस्।", "km":"គិតលុយ។", "si":"කරුණාකර බිල්පත දෙන්න.", "my":"ရှင်းမယ်။", "bn":"দয়া করে বিল দিন।", "lo":"ຄິດເງິນແດ່.", "ru":"Счет, пожалуйста.", "kz":"Есеп айырысайық."
    },
    {
        "cat":"Restaurant", "ko":"포장해 주세요.", "en":"To go, please.", 
        "vn":"Gói mang về nhé.", "cn":"请打包。", "th":"ห่อกลับบ้านค่ะ", "ph":"Paki-takeout.", "id":"Bungkus ya.", "jp":"持ち帰りにしてください。",
        "mn":"Авч явахаар боож өгөөч.", "uz":"Olib ketishga bering.", "ne":"कृपया प्याक गरिदिनुहोस्।", "km":"ខ្ចប់ទៅផ្ទះ។", "si":"කරුණාකර පාර්සල් කරන්න.", "my":"ပါဆယ်ထုပ်ပေးပါ။", "bn":"দয়া করে পার্সেল করে দিন।", "lo":"ຫໍ່ກັບບ້ານແດ່.", "ru":"С собой, пожалуйста.", "kz":"Өзіммен бірге алып кетемін."
    },
    {
        "cat":"Restaurant", "ko":"화장실 어디예요?", "en":"Where is the restroom?", 
        "vn":"Nhà vệ sinh đâu ạ?", "cn":"洗手间在哪里？", "th":"ห้องน้ำอยู่ไหนคะ", "ph":"Saan ang banyo?", "id":"Di mana toiletnya?", "jp":"トイレはどこですか？",
        "mn":"Ариун цэврийн өрөө хаана вэ?", "uz":"Hojatxona qayerda?", "ne":"शौचालय कहाँ छ?", "km":"តើបន្ទប់ទឹកនៅឯណា?", "si":"වැසිකිළිය කොහෙද?", "my":"အိမ်သာ ဘယ်မှာလဲ။", "bn":"টয়লেট কোথায়?", "lo":"ຫ້ອງນຳ້ຢູ່ໃສ?", "ru":"Где туалет?", "kz":"Дәретхана қайда?"
    },
    # --- AIRPORT (10 Questions) ---
    {
        "cat":"Airport", "ko":"여권을 보여주세요.", "en":"Passport, please.", 
        "vn":"Cho xem hộ chiếu.", "cn":"请出示护照。", "th":"ขอดูพาสปอร์ตหน่อยค่ะ", "ph":"Patingin ng passport.", "id":"Lihat paspornya.", "jp":"パスポートを見せてください。",
        "mn":"Гадаад паспортоо үзүүлнэ үү.", "uz":"Pasportingizni ko'rsating.", "ne":"कृपया राहदानी देखाउनुहोस्।", "km":"សូមបង្ហាញលិខិតឆ្លងដែន។", "si":"කරුණාකර විදේශ ගමන් බලපත්‍රය පෙන්වන්න.", "my":"နိုင်ငံကူးလက်မှတ်ပြပါ။", "bn":"দয়া করে পাসপোর্ট দেখান।", "lo":"ຂໍເບິ່ງພັດສະປອດແດ່.", "ru":"Паспорт, пожалуйста.", "kz":"Төлқұжатыңызды көрсетіңізші."
    },
    {
        "cat":"Airport", "ko":"탑승권 주세요.", "en":"Boarding pass, please.", 
        "vn":"Thẻ lên máy bay đâu ạ?", "cn":"请出示登机牌。", "th":"ขอดูบอร์ดดิ้งพาสค่ะ", "ph":"Boarding pass please.", "id":"Minta boarding pass.", "jp":"搭乗券をください。",
        "mn":"Суух тасалбараа үзүүлнэ үү.", "uz":"Chiptangizni bering.", "ne":"कृपया बोर्डिङ पास दिनुहोस्।", "km":"សូមបង្ហាញសំបុត្រយន្តហោះ។", "si":"කරුණාකර ගුවන් tikataya දෙන්න.", "my":"လေယာဉ်လက်မှတ်ပေးပါ။", "bn":"দয়া করে বোর্ডিং পাস দিন।", "lo":"ຂໍປີ້ຍົນແດ່.", "ru":"Посадочный талон, пожалуйста.", "kz":"Отырғызу талонын беріңізші."
    },
    {
        "cat":"Airport", "ko":"짐 찾는 곳이 어디예요?", "en":"Where is baggage claim?", 
        "vn":"Nơi nhận hành lý ở đâu?", "cn":"取行李的地方在哪里？", "th":"จุดรับกระเป๋าอยู่ที่ไหนคะ", "ph":"Saan ang baggage claim?", "id":"Di mana pengambilan bagasi?", "jp":"手荷物受取所はどこですか？",
        "mn":"Ачаа авах хэсэг хаана вэ?", "uz":"Yuk olish joyi qayerda?", "ne":"ब्यागेज क्लेम कहाँ छ?", "km":"តើកន្លែងយក វ៉ាលីនៅឯណា?", "si":"ගමන් මලු ලබා ගන්නා ස්ථානය කොහෙද?", "my":"အိတ်ယူရမယ့်နေရာ ဘယ်မှာလဲ။", "bn":"ব্যাগেজ ক্লেইম কোথায়?", "lo":"ບ່ອນຮັບກະເປົາຢູ່ໃສ?", "ru":"Где выдача багажа?", "kz":"Жүк алатын жер қайда?"
    },
    {
        "cat":"Airport", "ko":"비행기가 연착됐어요.", "en":"Flight is delayed.", 
        "vn":"Chuyến bay bị hoãn.", "cn":"航班延误了。", "th":"เที่ยวบินล่าช้าค่ะ", "ph":"Delayed ang flight.", "id":"Penerbangan ditunda.", "jp":"飛行機が遅れています。",
        "mn":"Нислэг хойшлогдсон.", "uz":"Parvoz kechiktirildi.", "ne":"उडान ढिला भयो।", "km":"ជើងហោះហើរត្រូវបានពន្យារពេល។", "si":"ගුවන් ගමන ප්‍රමාදයි.", "my":"လေယာဉ်နောက်ကျနေတယ်။", "bn":"ফ্লাইট বিলম্বিত হয়েছে।", "lo":"ຖ້ຽວບິນຊັກຊ້າ.", "ru":"Рейс задержан.", "kz":"Рейс кешіктірілді."
    },
    {
        "cat":"Airport", "ko":"환전소가 어디예요?", "en":"Where is currency exchange?", 
        "vn":"Đổi tiền ở đâu?", "cn":"货币兑换处在哪里？", "th":"ที่แลกเงินอยู่ที่ไหนคะ", "ph":"Saan ang palitan ng pera?", "id":"Di mana penukaran uang?", "jp":"両替所はどこですか？",
        "mn":"Валют солилцох цэг хаана вэ?", "uz":"Valyuta ayirboshlash shoxobchasi qayerda?", "ne":"मुद्रा विनिमय कहाँ छ?", "km":"តើកន្លែងប្តូរប្រាក់នៅឯណា?", "si":"මුදල් හුවමාරුව කොහෙද?", "my":"ငွေလဲကောင်တာ ဘယ်မှာလဲ။", "bn":"মুদ্রা বিনিময় কোথায়?", "lo":"ບ່ອນແລກປ່ຽນເງິນຢູ່ໃສ?", "ru":"Где обмен валюты?", "kz":"Ақша айырбастау орны қайда?"
    },
    {
        "cat":"Airport", "ko":"창가 좌석 주세요.", "en":"Window seat, please.", 
        "vn":"Cho tôi ghế cạnh cửa sổ.", "cn":"请给我靠窗的座位。", "th":"ขอนั่งริมหน้าต่างค่ะ", "ph":"Gusto ko sa window seat.", "id":"Minta kursi dekat jendela.", "jp":"窓側の席をお願いします。",
        "mn":"Цонхны дэргэд сууя.", "uz":"Deraza yonidan joy bering.", "ne":"कृपया झ्यालको सिट दिनुहोस्।", "km":"សុំកៅអីក្បែរបង្អួច។", "si":"කරුණාකර ජනේලය අසල ආසනයක් දෙන්න.", "my":"ပြတင်းပေါက်နား ထိုင်ခုံပေးပါ။", "bn":"দয়া করে জানালার পাশের সিট দিন।", "lo":"ຂໍບ່ອນນັ່ງແຄມປ່ອງຢ້ຽມແດ່.", "ru":"Место у окна, пожалуйста.", "kz":"Терезе жанынан орын беріңізші."
    },
    {
        "cat":"Airport", "ko":"가방을 잃어버렸어요.", "en":"I lost my bag.", 
        "vn":"Tôi bị mất túi.", "cn":"我的包丢了。", "th":"ทำกระเป๋าหายค่ะ", "ph":"Nawala ang bag ko.", "id":"Tas saya hilang.", "jp":"鞄をなくしました。",
        "mn":"Би цүнхээ гээчихлээ.", "uz":"Men sumkamni yo'qotib qo'ydim.", "ne":"मैले मेरो झोला हराएँ।", "km":"ខ្ញុំបាត់កាបូប។", "si":"මට මගේ බෑගය නැති වුණා.", "my":"အိတ်ပျောက်သွားတယ်။", "bn":"আমি আমার ব্যাগ হারিয়েছি।", "lo":"ຂ້ອຍເສຍກະເປົາ.", "ru":"Я потерял сумку.", "kz":"Сөмкемді жоғалтып алдым."
    },
    {
        "cat":"Airport", "ko":"게이트가 어디예요?", "en":"Where is the gate?", 
        "vn":"Cổng ra ở đâu?", "cn":"登机口在哪里？", "th":"เกตอยู่ที่ไหนคะ", "ph":"Saan ang gate?", "id":"Di mana gerbangnya?", "jp":"ゲートはどこですか？",
        "mn":"Гарц хаана вэ?", "uz":"Darvoza qayerda?", "ne":"गेट कहाँ छ?", "km":"តើច្រកចេញនៅឯណា?", "si":"ගේට්ටුව කොහෙද?", "my":"ဂိတ်ပေါက် ဘယ်မှာလဲ။", "bn":"গেট কোথায়?", "lo":"ປະຕູທາງອອກຢູ່ໃສ?", "ru":"Где выход на посадку?", "kz":"Шыгу қақпасы қайда?"
    },
    {
        "cat":"Airport", "ko":"출국 심사는 어디죠?", "en":"Where is immigration?", 
        "vn":"Nhập cảnh ở đâu?", "cn":"移民局在哪里？", "th":"ตม. อยู่ที่ไหนคะ", "ph":"Saan ang immigration?", "id":"Di mana imigrasi?", "jp":"入国審査はどこですか？",
        "mn":"Шилжилт хөдөлгөөн хаана вэ?", "uz":"Immigratsiya qayerda?", "ne":"अध्यागमन कहाँ छ?", "km":"តើអន្តោប្រវេសន៍នៅឯណា?", "si":"ආගමන විගමන කාර්යාලය කොහෙද?", "my":"လူဝင်မှုကြီးကြပ်ရေး ဘယ်မှာလဲ။", "bn":"ইমিগ্রেশন কোথায়?", "lo":"ບ່ອນກວດຄົນເຂົ້າເມືອງຢູ່ໃສ?", "ru":"Где паспортный контроль?", "kz":"Паспорттық бақылау қайда?"
    },
    {
        "cat":"Airport", "ko":"면세점이 어디예요?", "en":"Where is duty free?", 
        "vn":"Cửa hàng miễn thuế đâu?", "cn":"免税店在哪里？", "th":"ร้านปลอดภาษีอยู่ไหนคะ", "ph":"Saan ang duty free?", "id":"Di mana duty free?", "jp":"免税店はどこですか？",
        "mn":"Татваргүй барааны дэлгүүр хаана вэ?", "uz":"Duty free qayerda?", "ne":"ड्युटी फ्री कहाँ छ?", "km":"តើហាងរួចពន្ធនៅឯណា?", "si":"තීරුබදු රහිත සාප්පුව කොහෙද?", "my":"အφοွန်လွတ်ဆိုင် ဘယ်မှာလဲ။", "bn":"ডিউটি ​​ফ্রি কোথায়?", "lo":"ຮ້ານປອດພາສີຢູ່ໃສ?", "ru":"Где дьюти-фри?", "kz":"Дьюти-фри қайда?"
    }
])

ALL_LANGS = ['ko', 'vn', 'cn', 'th', 'ph', 'id', 'mn', 'uz', 'ne', 'km', 'si', 'my', 'bn', 'lo', 'ru', 'en', 'jp', 'kz']

def get_ui(lang, key):
    if lang in UI_TEXT and key in UI_TEXT[lang]: return UI_TEXT[lang][key]
    if 'en' in UI_TEXT and key in UI_TEXT['en']: return UI_TEXT['en'][key]
    if 'ko' in UI_TEXT and key in UI_TEXT['ko']: return UI_TEXT['ko'][key]
    return key

for lang in ALL_LANGS:
    ui_obj = {}
    base_keys = ['appName', 'appDesc', 'slogan', 'check', 'nativeLabel', 'selectTarget', 'title', 'start', 'back', 
                 'listening', 'placeholder', 'msgPerfect', 'msgGood', 'msgBad', 'correction', 'listen', 'why', 'aiName',
                 'selectStep', 'speakStep',
                 'btnFeedback', 'feedbackTitle', 'phFeedback', 'phContact', 'btnSend', 'btnClose', 'msgSent',
                 'cat_School', 'cat_Travel', 'cat_Hospital', 'cat_Market', 'cat_Restaurant', 'cat_Airport']
    for k in base_keys:
        ui_obj[k] = get_ui(lang, k)
        
    content_obj = { 'School': [], 'Travel': [], 'Hospital': [], 'Market': [], 'Restaurant': [], 'Airport': [] }
    
    for q in QUESTIONS:
        cat = q['cat']
        text = ""
        # Priority: Exact Lang -> En -> Ko
        if lang in q and q[lang]:
            text = q[lang]
        elif 'en' in q and q['en']:
            text = q['en']
        else:
            text = q.get('ko', '...')
        
        content_obj[cat].append(text)
        
    final_obj = { 'ui': ui_obj, 'content': content_obj }
    
    file_path = os.path.join(OUTPUT_DIR, f"{lang}.js")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("window.GLOTO = window.GLOTO || {};\n")
        f.write("window.GLOTO.DATA = window.GLOTO.DATA || {};\n\n")
        f.write(f"window.GLOTO.DATA['{lang}'] = ")
        f.write(json.dumps(final_obj, indent=4, ensure_ascii=False))
        f.write(";\n")
    
    print(f"Generated {file_path}")
