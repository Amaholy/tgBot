# keyboards.py
from telebot import types
import config

# 1. Главное меню
def create_main_menu():
    """Создает главное меню."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("1. Обучение для новичков", callback_data='menu_1'),
        types.InlineKeyboardButton("2. Юридический блок", callback_data='menu_2'),
        types.InlineKeyboardButton("3. Объекты СКОР", callback_data='menu_3'),
        types.InlineKeyboardButton("4. Ипотечный блок", callback_data='menu_4'),
        types.InlineKeyboardButton("5. Текущие новостройки", callback_data='menu_5'),
        types.InlineKeyboardButton("6. Загородная недвижимость", callback_data='menu_6'), 
        types.InlineKeyboardButton("7. Маркетинг", callback_data='menu_7'),
        types.InlineKeyboardButton("8. Прайс-лист на услуги компании", url=config.PRICELIST_URL),
        types.InlineKeyboardButton("9. УТП Компании", url=config.UTP_URL)
    )
    return markup

# 2. Меню "2. Юридический блок" - Уровень 1 (L1)
def create_legal_menu_l1():
    """Подменю Юридический блок (Уровень 1)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Список документов необходимые для сделки", callback_data='legal_l1_docs_list'),
        types.InlineKeyboardButton("Агентские договоры", callback_data='legal_l1_agency_agreements'),
        types.InlineKeyboardButton("Соглашение о задатке", callback_data='legal_l1_deposit_agreement'),
        types.InlineKeyboardButton("Дополнительные соглашения к задатку", callback_data='legal_l1_additional_agreements'),
        types.InlineKeyboardButton("Соглашение о расторжении задатка", callback_data='legal_l1_termination_agreement'),
        types.InlineKeyboardButton("Разные документы", callback_data='legal_l1_various_docs'),
        types.InlineKeyboardButton("Соглашение о задатке онлайн", callback_data='legal_l1_online_deposit'),
        types.InlineKeyboardButton("Инструкции, памятки и алгоритмы", callback_data='legal_l1_instructions'),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.1. Список документов необходимые для сделки - Уровень 2 (L2)
def create_docs_list_menu_l2():
    """Подменю Список документов необходимые для сделки (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Пакет докуметов на всех этапах сделки", url=config.DOCS_DEAL_PACKAGE_URL),
        types.InlineKeyboardButton("Документ для соглашения о задатке", url=config.DOCS_DEPOSIT_AGREEMENT_URL),
        types.InlineKeyboardButton("Список документов для договора купли-продажи", url=config.DOCS_PURCHASE_AGREEMENT_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.2. Агентские договоры - Уровень 2 (L2)
def create_agency_agreements_menu_l2():
    """Подменю Агентские договоры (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("На покупателя", callback_data='legal_l2_for_buyer'),
        types.InlineKeyboardButton("На продавца", callback_data='legal_l2_for_seller'),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.2.1. На покупателя - Уровень 3 (L3)
def create_buyer_agreements_menu_l3():
    """Подменю На покупателя (Уровень 3)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Договор покупателю", url=config.AGREEMENT_BUYER_URL),
        types.InlineKeyboardButton("Реестр на осмотр ИП Ястребова", url=config.INSPECTION_REGISTER_YASTREBOVA_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_agency_agreements_l2'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.2.2. На продавца - Уровень 3 (L3)
def create_seller_agreements_menu_l3():
    """Подменю На продавца (Уровень 3)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Договор продавцу", url=config.AGREEMENT_SELLER_URL),
        types.InlineKeyboardButton("Соглашение о передаче ключей от объекта недвижимости", url=config.KEY_TRANSFER_AGREEMENT_URL),
        types.InlineKeyboardButton("Приложение 1 Продавцу", url=config.ANNEX_1_SELLER_URL),
        types.InlineKeyboardButton("Эксклюзивный договор продавцу", url=config.EXCLUSIVE_AGREEMENT_SELLER_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_agency_agreements_l2'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.3. Соглашение о задатке - Уровень 2 (L2)
def create_deposit_agreement_menu_l2():
    """Подменю Соглашение о задатке (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Задаток пустой бланк", url=config.DEPOSIT_BLANK_URL),
        types.InlineKeyboardButton("Задаток пустой бланк без Этажей", url=config.DEPOSIT_BLANK_WITHOUT_ETAGI_URL),
        types.InlineKeyboardButton("Задаток пустой бланк по доверенности", url=config.DEPOSIT_BLANK_POWER_OF_ATTORNEY_URL),
        types.InlineKeyboardButton("Соглашение о задатке виде расписки", url=config.DEPOSIT_RECEIPT_URL),
        types.InlineKeyboardButton("Задаток на компанию пустой бланк", url=config.DEPOSIT_COMPANY_BLANK_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.4. Дополнительные соглашения к задатку - Уровень 2 (L2)
def create_additional_agreements_menu_l2():
    """Подменю Дополнительные соглашения к задатку (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Соглашение на увеличение суммы задатка", url=config.ADD_AGREEMENT_INCREASE_URL),
        types.InlineKeyboardButton("Соглашение продление срока задатка", url=config.ADD_AGREEMENT_EXTENSION_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.5. Соглашение о расторжении задатка - Уровень 2 (L2)
def create_termination_agreement_menu_l2():
    """Подменю Соглашение о расторжении задатка (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Расторжение в связи с отказом банка", url=config.TERMINATION_BANK_REFUSAL_URL),
        types.InlineKeyboardButton("Расторжение по вине покупателя", url=config.TERMINATION_BUYER_FAULT_URL),
        types.InlineKeyboardButton("Расторжение по вине продавца", url=config.TERMINATION_SELLER_FAULT_URL),
        types.InlineKeyboardButton("Расторжение по обоюдному", url=config.TERMINATION_MUTUAL_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.6. Разные документы - Уровень 2 (L2)
def create_various_docs_menu_l2():
    """Подменю Разные документы (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("АРЕНДА поиск Арендатора", url=config.LEASE_TENANT_SEARCH_URL),
        types.InlineKeyboardButton("АРЕНДА поиск Объекта", url=config.LEASE_OBJECT_SEARCH_URL),
        types.InlineKeyboardButton("ДВОУ по ипотеке", url=config.DCOU_MORTGAGE_URL),
        types.InlineKeyboardButton("ДВОУ по снятию ЕПВ", url=config.DCOU_EPV_WITHDRAWAL_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.7. Соглашение о задатке онлайн - Уровень 2 (L2)
def create_online_deposit_menu_l2():
    """Подменю Соглашение о задатке онлайн (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Задаток онлайн пустой бланк", url=config.ONLINE_DEPOSIT_BLANK_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# 2.8. Инструкции, памятки и алгоритмы - Уровень 2 (L2)
def create_instructions_menu_l2():
    """Подменю Инструкции, памятки и алгоритмы (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Инструкция по подписанию документов", url=config.INSTRUCTIONS_SIGNING_DOCS_URL),
        types.InlineKeyboardButton("Онлайн подписание Памятка для клиентов", url=config.ONLINE_SIGNING_MEMO_URL),
        types.InlineKeyboardButton("Подача заявки на договор в юр.отдел", url=config.LEGAL_DEPT_APPLICATION_URL),
        types.InlineKeyboardButton("Доход от продажи недвижимости", url=config.PROPERTY_SALE_INCOME_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_legal_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

# --- ОСТАЛЬНЫЕ МЕНЮ (СОХРАНЕНЫ ДЛЯ ПОЛНОТЫ) ---

def create_score_menu():
    """Подменю Объекты СКОР."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Список объектов СКОР и ссылки", url=config.SCORE_LIST_URL),
        types.InlineKeyboardButton("Как завести недвижимость в СКОР", url=config.SCORE_HOWTO_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_rural_menu():
    """Подменю Загородная недвижимость."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Чек лист о загородной недвижимости", url=config.RURAL_CHECKLIST_URL),
        types.InlineKeyboardButton("Сайт о расположении и описание земельных участков РК", url=config.RURAL_RK_PLOTS_URL),
        types.InlineKeyboardButton("Ген. План застройки Костанайский р-н", url=config.RURAL_KOSTANAY_PLAN_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_novice_menu_l1():
    """Подменю Обучение для новичков (Уровень 1)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Скрипты", url=config.SCRIPTS_URL),
        types.InlineKeyboardButton("Бизнес Этика", url=config.BUSINESS_ETHICS_URL),
        types.InlineKeyboardButton("Вторичный рынок", url=config.SECONDARY_MARKET_URL),
        types.InlineKeyboardButton("Загородная недвижимость", url=config.RURAL_NOVICE_URL),
        types.InlineKeyboardButton("Личный бренд", url=config.PERSONAL_BRAND_URL),
        types.InlineKeyboardButton("Новостройки", url=config.NEW_BUILDINGS_URL),
        types.InlineKeyboardButton("Оценка", url=config.APPRAISAL_URL),
        types.InlineKeyboardButton("Работа с возражениями", url=config.OBJECTIONS_URL),
        types.InlineKeyboardButton("EGOV", url=config.EGOV_URL),
        types.InlineKeyboardButton("Работа в системах РИЕС и CRM", callback_data='novice_l1_ries'), 
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_ries_crm_menu_l2():
    """Подменю РИЕС/CRM (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Закрытие сделки", url=config.DEAL_CLOSURE_URL),
        types.InlineKeyboardButton("Окна риелтора", url=config.REALTOR_WINDOWS_URL),
        types.InlineKeyboardButton("Задаток и сделка в системе", url=config.DEPOSIT_AND_DEAL_URL),
        types.InlineKeyboardButton("Как отменить показ", url=config.CANCEL_SHOWING_URL),
        types.InlineKeyboardButton("Как удалить фотографии", url=config.DELETE_PHOTOS_URL),
        types.InlineKeyboardButton("Как фотографии добавить через РИЕС", url=config.ADD_PHOTOS_RIES_URL),
        types.InlineKeyboardButton("Как сделать обрисовку", url=config.OUTLINE_RIES_URL),
        types.InlineKeyboardButton("Подтверждение показа", url=config.SHOWING_CONFIRMATION_URL),
        types.InlineKeyboardButton("Поиск объектов по фильтру в мобильном РИЕС", url=config.SEARCH_MOBILE_RIES_URL),
        types.InlineKeyboardButton("Создание заявки в мобильном РИЕС", url=config.CREATE_APP_MOBILE_RIES_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_novice_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_marketing_menu_l1():
    """Подменю Маркетинг (Уровень 1)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Где найти и как привлечь клиентов", url=config.CLIENTS_ATTRACTION_URL),
        types.InlineKeyboardButton("Формирование входящего потока. Курс Реэлтор Базовый", url=config.INFLOW_COURSE_URL),
        types.InlineKeyboardButton("Методичка.Тренинг", url=config.METHODIC_TRAINING_URL),
        types.InlineKeyboardButton("Макеты для соц.сетей", url=config.SOCIAL_MEDIA_LAYOUTS_URL),
        types.InlineKeyboardButton("Конструктор макетов расклейки", url=config.PASTE_LAYOUT_CONSTRUCTOR_URL),
        types.InlineKeyboardButton("Ссылки на отзывы", callback_data='marketing_l1_reviews'),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_reviews_menu_l2():
    """Подменю Ссылки на отзывы (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("2gis", url=config.REVIEWS_2GIS_URL),
        types.InlineKeyboardButton("Google", url=config.REVIEWS_GOOGLE_URL),
        types.InlineKeyboardButton("Яндекс", url=config.REVIEWS_YANDEX_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_marketing_l1'), 
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_mortgage_menu_l1():
    """Подменю Ипотечный блок (Уровень 1)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Скрипт для риэлтеров - ипотека", url=config.MORTGAGE_SCRIPT_URL),
        types.InlineKeyboardButton("Комиссии банков при снятии денежных средств", url=config.BANK_COMMISSION_URL),
        types.InlineKeyboardButton("Список оценочных компании", url=config.APPRAISAL_COMPANIES_URL),
        types.InlineKeyboardButton("Шпаргалка по банкам Казахстан", url=config.KAZAKHSTAN_BANK_CHEAT_SHEET_URL),
        types.InlineKeyboardButton("Обучение для ипотечного брокера", callback_data='mortgage_l1_broker_training'),
        types.InlineKeyboardButton("Залоговая политика банков", url=config.COLLATERAL_POLICY_URL),
        types.InlineKeyboardButton("Важные контактные данные", url=config.CONTACT_DATA_URL),
        types.InlineKeyboardButton("Карта сделки", callback_data='mortgage_l1_deal_map'),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_broker_training_menu_l2():
    """Подменю Обучение для ипотечного брокера (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Тетрадь ипотечного брокера", url=config.BROKER_NOTEBOOK_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_mortgage_l1'), 
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_deal_map_menu_l2():
    """Подменю Карта сделки (Уровень 2)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("БЦК Этапы", url=config.DEAL_MAP_BCC_URL),
        types.InlineKeyboardButton("Отбасы карта сделки", url=config.DEAL_MAP_OTBASY_URL),
        types.InlineKeyboardButton("Фридом этапы сделки", url=config.DEAL_MAP_FREEDOM_URL),
        types.InlineKeyboardButton("Карта сделки Форте банк", url=config.DEAL_MAP_FORTE_URL),
        types.InlineKeyboardButton("Карта сделки Халык банк", url=config.DEAL_MAP_HALYK_URL),
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_mortgage_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_new_buildings_menu_l1():
    """Подменю Текущие новостройки (Уровень 1)."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Общие ссылки
    markup.add(
        types.InlineKeyboardButton("Общая информация о жилых комплексах", url=config.NEW_BUILDINGS_GENERAL_INFO_URL),
        types.InlineKeyboardButton("Квартира от ИНВЕСТОРА", url=config.NEW_BUILDINGS_INVESTOR_URL),

    )
    
    # Кнопки для конкретных ЖК
    for key, data in config.NEW_BUILDINGS_DATA.items():
        markup.add(types.InlineKeyboardButton(data["name"], callback_data=f'jk_detail_{key}'))
        
    # Кнопки навигации
    markup.add(
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup

def create_jk_detail_menu_l2(jk_key):
    """Подменю для конкретного ЖК (Уровень 2)."""
    jk_data = config.NEW_BUILDINGS_DATA.get(jk_key)
    
    if not jk_data:
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
        )
        return markup
        
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Кнопка Шахматка
    if "board_url" in jk_data and jk_data["board_url"]:
        markup.add(types.InlineKeyboardButton("📊 Шахматка", url=jk_data["board_url"]))
    
    # Кнопка Информация
    if "info_url" in jk_data and jk_data["info_url"]:
        markup.add(types.InlineKeyboardButton("📝 Информация по новостройке", url=jk_data["info_url"]))
        
    # Новая кнопка Прайс цены (появится только если есть ссылка в конфиге)
    if "price_url" in jk_data and jk_data["price_url"]:
        markup.add(types.InlineKeyboardButton("💰 Прайс цены", url=jk_data["price_url"]))

    markup.add(
        types.InlineKeyboardButton("⬅️ Назад", callback_data='back_to_new_buildings_l1'),
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    return markup