
import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env, если он есть рядом
load_dotenv()

# --- ТОКЕН И КОД ДОСТУПА ---
# Бот сначала ищет токен в .env файле. 
# Если его там нет (например, на сервере), он берет его из системных переменных.
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN не задан. Укажите его в файле .env')
ACCESS_CODE = '1122'
# Для локального запуска оставьте пустым. На сервере, если нужен SOCKS:
# PROXY_URL=socks5h://127.0.0.1:40000
PROXY_URL = os.getenv('PROXY_URL', '')

# --- ССЫЛКИ ДЛЯ МЕНЮ ---

# Объекты СКОР (3)
SCORE_LIST_URL = 'https://docs.google.com/spreadsheets/d/17QDnuBxyhJgPiLsNDaTfEYCssaZLDYGd/edit#gid=1590113260'
SCORE_HOWTO_URL = 'https://docs.google.com/presentation/d/1A2Bob-WamUJ8gguTDFL9xzj-CYXhhIQD/edit#slide=id.p1'

# Загородная недвижимость (6)
RURAL_CHECKLIST_URL = 'https://drive.google.com/uc?export=download&id=1aA9cPnqGPWiKQzLPnjiLlUBg14uNDKLx'
RURAL_RK_PLOTS_URL = 'https://map.gov4c.kz/egkn/'
RURAL_KOSTANAY_PLAN_URL = 'https://drive.google.com/drive/folders/1VVibgUyGKzGoNjED8fs9el8nvtBulOfD'

# Обучение для новичков (1) - Уровень 1
SCRIPTS_URL = 'https://docs.google.com/document/d/1vzBDxD1IFu520c-XAL90DgJZVKQg8lSk/edit'
BUSINESS_ETHICS_URL = 'https://docs.google.com/presentation/d/1uf7hWWWDKIbqa6WFhlItmXQ2Bgm1N71n/edit#slide=id.p1'
SECONDARY_MARKET_URL = 'https://docs.google.com/presentation/d/1dIii7Zbi3oxy9rGdCSwZYMW0xbpn-Ujp/edit#slide=id.p1'
RURAL_NOVICE_URL = 'https://docs.google.com/presentation/d/1E3WIZmx1Wauie7zjFey4njTstp2nnCYc/edit#slide=id.p1'
PERSONAL_BRAND_URL = 'https://docs.google.com/presentation/d/1eQd29dIxbrFVgPcyMYyyw-1qhEBEPOfH/edit#slide=id.p1'
NEW_BUILDINGS_URL = 'https://docs.google.com/presentation/d/15hUFOBqWhMUwF7tg0RBRMwCOIsCezti6/edit#slide=id.p1'
APPRAISAL_URL = 'https://docs.google.com/presentation/d/15hUFOBqWhMUwF7tg0RBRMwCOIsCezti6/edit#slide=id.p1'
OBJECTIONS_URL = 'https://docs.google.com/presentation/d/1H1dQ5g_5poPzqeFb2Mj8voeM4vGskUP2/edit#slide=id.p1'
EGOV_URL = 'https://drive.google.com/drive/folders/1mupWPuTnuXu9jdpl3tmGqLjMpX7m9YBg'

# Обучение для новичков (1) - Уровень 2 (Работа в системах РИЕС и CRM)
DEAL_CLOSURE_URL = 'https://drive.google.com/drive/folders/1gQ1KTSfdGxRBDEvA6x-VQ8df_SDFzxVV'
REALTOR_WINDOWS_URL = 'https://docs.google.com/document/d/1rvN_kEbSQjsLC1igkSnRO4ay_WDiAth_/edit'
DEPOSIT_AND_DEAL_URL = 'hhttps://drive.google.com/drive/folders/1gQ1KTSfdGxRBDEvA6x-VQ8df_SDFzxVV'
CANCEL_SHOWING_URL = 'https://drive.google.com/file/d/1pYso9chCBl-e89JqktV-1Abpv5wMCDYl/view?usp=sharing'
DELETE_PHOTOS_URL = 'https://drive.google.com/file/d/1uTdX_AA1rRaDZFHIrQY7PhTkNJDkXwFK/view?usp=sharing'
ADD_PHOTOS_RIES_URL = 'https://drive.google.com/file/d/1JixqV2IIpBi_Q4e4NAmrS9lR8qQaJsP8/view?usp=sharing'
OUTLINE_RIES_URL = 'https://drive.google.com/file/d/1sRS66UX8yIZDMfQTc66FVbd8l8yxJJTl/view?usp=sharing'
SHOWING_CONFIRMATION_URL = 'https://drive.google.com/file/d/1uGy69Z7jzHRkpoIwvbmoSaaNq8VB_bUa/view?usp=sharing'
SEARCH_MOBILE_RIES_URL = 'https://drive.google.com/file/d/1ob2OxwZImlYhxqu3Og89rbmmqrZj1UWA/view?usp=sharing'
CREATE_APP_MOBILE_RIES_URL = 'https://drive.google.com/file/d/1ob2OxwZImlYhxqu3Og89rbmmqrZj1UWA/view?usp=sharing'

# Главное меню (8 и 9)
PRICELIST_URL = 'https://docs.google.com/spreadsheets/d/1MvyyS5IKeqoO5Lk_abPkOd6SP3sfbcSMTt7Tr3L_pWA/edit#gid=328449685'
UTP_URL = 'https://docs.google.com/spreadsheets/d/106K17gorq7K_Huwc4eqjD1rN6k3i_elPWRa7flyjpZc/edit#gid=0'

# Маркетинг (7) - Уровень 1
CLIENTS_ATTRACTION_URL = 'https://docs.google.com/presentation/d/15YTVsZc4ZA2T2PkjjSHo-DklSsLWmBcn/edit?usp=sharing&ouid=118107650400863849368&rtpof=true&sd=true'
INFLOW_COURSE_URL = 'https://docs.google.com/presentation/d/1nKjsAYFe9G6Fjs3QU8tM0cF60tU0SF5e/edit?usp=sharing&ouid=118107650400863849368&rtpof=true&sd=true'
METHODIC_TRAINING_URL = 'https://docs.google.com/document/d/1MchwZLVNADQ3So77HC_km2iwKBwwua7b/edit?usp=sharing&ouid=118107650400863849368&rtpof=true&sd=true'
SOCIAL_MEDIA_LAYOUTS_URL = 'https://t.me/+NwltsTTXeEZlOTFi' # TG channel
PASTE_LAYOUT_CONSTRUCTOR_URL = 'https://docs.google.com/presentation/d/1ckzmF3u9VE-xrtTtl_cRefpX0p7mla_1/edit?usp=sharing&ouid=104195346317833818544&rtpof=true&sd=true'

# Маркетинг (7) - Уровень 2 (Ссылки на отзывы)
REVIEWS_2GIS_URL = 'https://2gis.kz/kostanay/firm/70000001041074486'
REVIEWS_GOOGLE_URL = 'https://www.google.kz/maps/place/Этажи/@53.2199249,63.6225047,17z/data=!3m1!4b1!4m5!3m4!1s0x43cc8b6581f4ee73:0x48e57325416f5306!8m2!3d53.2199249!4d63.6225047?hl=ru'
REVIEWS_YANDEX_URL = 'https://yandex.kz/maps/org/128535523648/?ll=63.622470%2C53.219980&mode=search&sll=67.312870%2C53.760755&sspn=65.379756%2C21.315542&text=Этажи костанай&z=16'

# Ипотечный блок (4) - Уровень 1
MORTGAGE_SCRIPT_URL = 'https://docs.google.com/spreadsheets/d/1oD8vdZI0SEz71Ik8vF6h_2k7BpiNgzJM/edit#gid=1623508721'
BANK_COMMISSION_URL = 'https://drive.google.com/file/d/1eilDwscq_zGIZr2mDz9O0_telrjR8Guv/view?usp=sharing'
APPRAISAL_COMPANIES_URL = 'https://docs.google.com/spreadsheets/d/17N6xtUHzd90aFNtw1g2zQTSeMQKass9F/edit?usp=sharing&ouid=118107650400863849368&rtpof=true&sd=true'
KAZAKHSTAN_BANK_CHEAT_SHEET_URL = 'https://docs.google.com/spreadsheets/d/1p60JJg5j-jr1q2NZf72azbme7WxCMU1k/edit?gid=884968483#gid=884968483'
COLLATERAL_POLICY_URL = 'https://docs.google.com/spreadsheets/d/1SFnfNR2-_colMOe2030AVtlhzYFhHMT5/edit?gid=602142262#gid=602142262'
CONTACT_DATA_URL = 'https://docs.google.com/spreadsheets/d/151QM0wAEkAyQvy5hR3DAibSvyHT3AH0l/edit?gid=5669678#gid=5669678'

# Ипотечный блок (4) - Уровень 2 (Обучение для ипотечного брокера)
BROKER_NOTEBOOK_URL = 'https://docs.google.com/document/d/15lt_OFTlyA5QD9qsmvetF_EbuubiKVp6/edit'

# Ипотечный блок (4) - Уровень 2 (Карта сделки)
DEAL_MAP_BCC_URL = 'https://docs.google.com/document/d/1stjyKhNFOlK3zjr_p2sSGkJwHFHK6Y6q/edit'
DEAL_MAP_OTBASY_URL = 'https://docs.google.com/document/d/1P9BD77Y20PuT9Y0on8zoGQIPkBZeetmx/edit'
DEAL_MAP_FREEDOM_URL = 'https://docs.google.com/document/d/1aLjc2m_eCg2yN3gyg62jVho4rNCbD2O2/edit#heading=h.gjdgxs'
DEAL_MAP_FORTE_URL = 'https://docs.google.com/presentation/d/1u8x44lpFLfvtLkWaNuccDt8nMYBybGK0/edit#slide=id.p1'
DEAL_MAP_HALYK_URL = 'https://docs.google.com/document/d/18VRlOQ8VwKHo9sckxEm4VtQ3hGDn2iij/edit?tab=t.0'

# Новостройки (5)
NEW_BUILDINGS_GENERAL_INFO_URL = 'https://docs.google.com/spreadsheets/d/1oLalulPKQSdw7XDgqEgyXFs8DK4N4gNxrmJsuDGSJtg/edit?gid=0#gid=0'
NEW_BUILDINGS_INVESTOR_URL = 'https://docs.google.com/spreadsheets/d/1k8AI8jUbfZe1qNpjTkBDetkQqVT9UkfO/edit?gid=1270461869#gid=1270461869'
NEW_BUILDINGS_DATA = {
    "jk_altynsarina": {"name": "ЖК Алтынсарина 228Б", "board_url": "https://docs.google.com/spreadsheets/d/1pr5LJH98dm-aa7gRs5b8myykYwnSl86vy7aw65N3XX0/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/u/0/folders/1su2YlEDcVCSGfjnHx_Y9nazaLrNVE69n"},
    "jk_kairbekova": {"name": "ЖК Каирбекова 83", "board_url": "https://docs.google.com/spreadsheets/d/1Pd3AVYmbEsVvsidAmkr32Hj0jMFWOnOPIxcd--fuCio/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/u/0/folders/1rwBI0wpAk6PuZMn5j7RqNPMvymImW1bd"},
    "jk_green_park": {"name": "ЖК Green Park", "board_url": "https://docs.google.com/spreadsheets/d/1WpYLCyu_QF3DAbq3nwAmeqiKjXivRiUFkbBzyJOtUQk/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/u/0/folders/1H-gOFsIKIHdq1xWypdPTuyqxy67W6hip"},
    "jk_vasilievsky": {"name": "ЖК Васильевский", "board_url": "https://docs.google.com/spreadsheets/d/10pE-52-JRBeKQkmElXJ0trdX5vFL_QkhEsiiUM4CBP0/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/u/0/folders/1TsCMpSODoYUZf0NOZql1TKxS3BoY8VRv"},
    "jk_kievskaya": {"name": "ЖК Киевская 7/2", "board_url": "https://docs.google.com/spreadsheets/d/1jDfWHfLu1W-DKI4eKUKIzJd7om7fm55V/edit?gid=1347023797#gid=1347023797", "info_url": "https://drive.google.com/drive/folders/1pdraXY66JL3wo3hu9qDg4Dmjntzu7sWZ"},
    "jk_park_house": {"name": "ЖК Park House", "board_url": "https://docs.google.com/spreadsheets/d/1cT2EjSvhw8qKaVe7s_3PYFEnFMRlPxPpesWuN5wkyUo/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/u/0/folders/1xQuAL9P3dftPaSqgJDG_Vzd9yUQW4OLv"},
    "jk_pushkina": {"name": "ЖК Пушкина 1 и 3", "info_url": "https://drive.google.com/drive/folders/14NPEDsKg_smNp11fbHzwa4xs7ErPiERA"},
    "jk_rabata": {"name": "ЖК на Рабате",  "info_url": "https://drive.google.com/drive/folders/1Q8wKtuB76WT-wwyyqZVckxTPfkNqYKfN"},
    "jk_gagarin": {"name": "ЖК Гагарин Парк", "board_url": "https://docs.google.com/spreadsheets/d/1VsRg7EoGmzChbC9Ow082nz5SLsnohqS6YWeYaeRLzQs/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/folders/1cm2o8NVBybbnSd5TbeiOJRR2Xs0XgsOc", "price_url": "https://docs.google.com/spreadsheets/d/1BckXledXwTeHAMs-LqA52fB69DlAbfhi3mx6MFng_0M/edit?gid=0#gid=0"},
    "jk_kerei": {"name": "ЖК Керей комфорт", "board_url": "https://docs.google.com/spreadsheets/d/1VOEwx4-0LHBV-DxN_XASCktIIGLpJCajB-6MGC11q7M/edit?gid=0#gid=0", "info_url": "https://drive.google.com/drive/folders/1P8lWG6qO8P8qn_LiXkGJI3wlqT_YR4Uj"},
    "jk_tumar_comm": {"name": "Коммерция Тумар Резидентс", "info_url": "https://drive.google.com/drive/folders/1D1m7wSdAeBIKdnZl1v9XQxgJsI8Bpqi1"},
    "jk_tumar_3": {"name": "Тумар Резиденс 3", "info_url": "https://drive.google.com/drive/folders/1UHfuapK0Z5-P-UmkWfoVEebg_avEg7V-", "price_url": "https://docs.google.com/document/d/1g3nJLlWXYcITpDhX1bFTpXcz3dtjXO_s/edit"},
}

# --- ССЫЛКИ ДЛЯ ЮРИДИЧЕСКОГО БЛОКА (2) ---

# 2.1. Список документов необходимые для сделки (L2)
DOCS_DEAL_PACKAGE_URL = 'https://drive.google.com/uc?export=download&id=1pk-yQrswgDPE2TJdpg9iSdFIR5uJFyjW'
DOCS_DEPOSIT_AGREEMENT_URL = 'https://drive.google.com/uc?export=download&id=1ip98E1T3IHvtBXyZzSY38eMOC7KIU8vh'
DOCS_PURCHASE_AGREEMENT_URL = 'https://drive.google.com/uc?export=download&id=1PAjGqoOM_NTWK2hAa8e2uS_XGGLeBKh7'

# 2.2. Агентские договоры -> На покупателя (L3)
AGREEMENT_BUYER_URL = 'https://docs.google.com/document/d/1FPihJV9NzeUCu0QcFFPlhDfbSalSJAMX/edit'
INSPECTION_REGISTER_YASTREBOVA_URL = 'https://drive.google.com/uc?export=download&id=17UOoHNqVLDt0dIs_oG63IQ5lOEL52wAq'

# 2.2. Агентские договоры -> На продавца (L3)
AGREEMENT_SELLER_URL = 'https://docs.google.com/document/d/13jcPj9UdkGcolCD2fxSd0wkkI9FF9XDa/edit'
KEY_TRANSFER_AGREEMENT_URL = 'https://drive.google.com/uc?export=download&id=1Yf3feQrQBUUMdFJtNVfiSuxDVADrLpLz'
ANNEX_1_SELLER_URL = 'https://drive.google.com/uc?export=download&id=1Bhe_qvUTWsCKyFf_pVwu9V_tEvQtbRvF'
EXCLUSIVE_AGREEMENT_SELLER_URL = 'https://drive.google.com/uc?export=download&id=1xL42T7IZeKiybpvNZ69cwbSMoAfbJCbG'

# 2.3. Соглашение о задатке (L2)
DEPOSIT_BLANK_URL = 'https://drive.google.com/uc?export=download&id=1a62ochj03DqMOdff25PuIBI_9UgkFESG'
DEPOSIT_BLANK_WITHOUT_ETAGI_URL = 'https://drive.google.com/uc?export=download&id=1XAQBeyVrnkx0ug0oHTxpvhinHe9wXObt'
DEPOSIT_BLANK_POWER_OF_ATTORNEY_URL = 'https://drive.google.com/uc?export=download&id=1nVSPSsz34FIImrCV-qS69YzG0TNMIzcq'
DEPOSIT_RECEIPT_URL = 'https://drive.google.com/uc?export=download&id=11m0tJ-Rp6Lz7mTgvjjFutsIJT9I_Wq8L'
DEPOSIT_COMPANY_BLANK_URL = 'https://drive.google.com/uc?export=download&id=1BY4zJJoVAbQ_ZE0I28EGRw0E0PKxx0oQ'

# 2.4. Дополнительные соглашения к задатку (L2)
ADD_AGREEMENT_INCREASE_URL = 'https://drive.google.com/uc?export=download&id=1ijGprbyA1r-ofAmkcsqCqE416h8sKQgL'
ADD_AGREEMENT_EXTENSION_URL = 'https://drive.google.com/uc?export=download&id=1z3DGPTVn4dJI5ld5h7rrit4hfZFoKjyk'

# 2.5. Соглашение о расторжении задатка (L2)
TERMINATION_BANK_REFUSAL_URL = 'https://drive.google.com/uc?export=download&id=1N-olON9g63n6LhyiPMh6pHlIIq6tEZSS'
TERMINATION_BUYER_FAULT_URL = 'https://drive.google.com/uc?export=download&id=1CX42DgeSAqS4e6-JI-L0hlyWczFeQBZM'
TERMINATION_SELLER_FAULT_URL = 'https://drive.google.com/uc?export=download&id=1fZPeSUx3PnxGaCJoZSLq-S74glWBksuq'
TERMINATION_MUTUAL_URL = 'https://drive.google.com/uc?export=download&id=1yBQ9v0GUOZy_v6ItXK8DwIxY8MrjLR62'

# 2.6. Разные документы (L2)
LEASE_TENANT_SEARCH_URL = 'https://drive.google.com/uc?export=download&id=19hAuV8uKoRQtfJQSHYr_KqAinv1-5Lj-'
LEASE_OBJECT_SEARCH_URL = 'https://drive.google.com/uc?export=download&id=1itwfXxmWNCJurIb3uX2MVC3KeTzaKw8O'
DCOU_MORTGAGE_URL = 'https://drive.google.com/uc?export=download&id=1Uwd-AMOP74cqed9FZiqOf3r1ldQRVbna'
DCOU_EPV_WITHDRAWAL_URL = 'https://drive.google.com/uc?export=download&id=1cl4ZneYQrDtqux9Mo8vJDwItAM9dIeMD'

# 2.7. Соглашение о задатке онлайн (L2)
ONLINE_DEPOSIT_BLANK_URL = 'https://drive.google.com/uc?export=download&id=1vcYBRkzcdaiZnr2vN9rvYkH1rbdSm8HS'

# 2.8. Инструкции, памятки и алгоритмы (L2)
INSTRUCTIONS_SIGNING_DOCS_URL = 'https://drive.google.com/file/d/1Sth5lz7TXywEFC08ZykZFp6fZl6OT9q4/view?usp=share_link'
ONLINE_SIGNING_MEMO_URL = 'https://drive.google.com/file/d/1x5e3--AaZXNGu2PYip9tqe_u1sE6Oslt/view?usp=drive_link'
LEGAL_DEPT_APPLICATION_URL = 'https://drive.google.com/file/d/1AiNsA_3nuXsikcuPfT7I6lzP2dRIpF_4/view?usp=share_link'
PROPERTY_SALE_INCOME_URL = 'https://docs.google.com/document/d/1PChGlW7NU-Fd6rhdsrV_FDtEO76ePkDu/edit'

# --- ГОРОДА ---
CITY_KOSTANAY = 'kostanay'
CITY_TASHKENT = 'tashkent'


# --- ТАШКЕНТ ---

TASHKENT_PRICELIST_URL = 'https://docs.google.com/spreadsheets/d/1aUYY7RzpyagNxrWXSANQCCgFfu7WhbaH2lrFKqWYKko/edit?gid=0#gid=0'
TASHKENT_UTP_URL = 'https://docs.google.com/spreadsheets/d/1bkS1Nzmh9E1TN7YqL9VjnSjiC9v_eS5d/edit?gid=348717645#gid=348717645'

TASHKENT_CHECKLIST_COMMERCE_URL = 'https://docs.google.com/spreadsheets/d/1A-BFcMc1DFQIHn99xADhTQGKUqX-7Tys/edit?gid=1836360964#gid=1836360964'
TASHKENT_CHECKLIST_RURAL_URL = 'https://docs.google.com/document/d/1IFiB1SI-v2eV0VHLXilrNW4ZQ4VYtI0o/edit#heading=h.30j0zll'
TASHKENT_CHECKLIST_SECONDARY_URL = 'https://docs.google.com/document/d/1eeL-NZyEuvoHPJlKLxCiAB4jIMLLbG40/edit#heading=h.gjdgxs'
TASHKENT_CHECKLIST_BUYER_URL = 'https://docs.google.com/document/d/1uYKQV5uEMaVbiTFD5Dz8M2rM7gtnPF4h/edit'

TASHKENT_MARKETING_CLIENTS_URL = 'https://docs.google.com/presentation/d/15YTVsZc4ZA2T2PkjjSHo-DklSsLWmBcn/edit?slide=id.p26#slide=id.p26'
TASHKENT_MARKETING_INFLOW_URL = 'https://docs.google.com/presentation/d/1nKjsAYFe9G6Fjs3QU8tM0cF60tU0SF5e/edit?slide=id.p18#slide=id.p18'
TASHKENT_MARKETING_PASTE_LAYOUTS_URL = 'https://docs.google.com/presentation/d/19c-NNYLpPDWj2dL4WLsjXGaXm98Wm9qj/edit?slide=id.p65#slide=id.p65'
TASHKENT_MARKETING_SOCIAL_URLS = [
    'https://www.emrm.ru/storage/content/69aa8ed39a4096486b4eeefd',
    'https://www.emrm.ru/storage/content/69f0a02e2841b97fc79898f6?folder=69f1779b2841b97fc7989a8d',
    'https://www.emrm.ru/storage/content/6a1ea0512841b97fc7991456?folder=6a1ea0772841b97fc7991463',
]
TASHKENT_REVIEWS_URL = 'https://tashkent.etagi.com/feedback/'

TASHKENT_AGREEMENT_SELLER_URL = 'https://docs.google.com/document/d/1aKBlH_qjzwMU_uukuIAItp8-SsbHC2Oa/edit?usp=sharing&ouid=103131565268500743791&rtpof=true&sd=true'
TASHKENT_AGREEMENT_BUYER_URL = 'https://docs.google.com/document/d/1XCl-kAUMmMtRDNCD03Yz_JJ6Bo8vCd58/edit?usp=sharing&ouid=103131565268500743791&rtpof=true&sd=true'
TASHKENT_LEASE_AGREEMENT_URL = 'https://docs.google.com/document/d/18BN2jy3ZnlgpSem1QxoXXgTkaTukR2QV/edit?usp=sharing&ouid=103131565268500743791&rtpof=true&sd=true'
TASHKENT_ACT_SERVICES_URL = 'https://docs.google.com/document/d/16_hLhwoEhV_pDSVGPOAQON_qLHLTHB7M/edit'
TASHKENT_ACT_INSPECTION_URL = 'https://docs.google.com/document/d/1aq2ai0h-TdmCTLfixOOkyT8r967LK-Zh/edit'
TASHKENT_DEPOSIT_AGREEMENT_URL = 'https://docs.google.com/document/d/1emK0qAmHZusxlsJvBwDXgbRv0nEm6bVr/edit'
