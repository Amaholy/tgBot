# handlers.py
from telebot import types, TeleBot 
import config
import keyboards

# --- ФУНКЦИИ ОТОБРАЖЕНИЯ МЕНЮ ---

def show_main_menu(bot: TeleBot, chat_id: int, message_id: int=None):
    """Показывает Главное меню."""
    main_menu_text = (
        "Прокачайте свои навыки! Выберите что вам нужно:\n"
    )
    markup = keyboards.create_main_menu()
    if message_id:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=main_menu_text,
            reply_markup=markup,
            parse_mode='Markdown'
        )
    else:
        bot.send_message(chat_id, main_menu_text, reply_markup=markup, parse_mode='Markdown')

# 2. Меню "2. Юридический блок" - Уровень 1 (L1)
def show_legal_menu_l1(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Юридический блок (Уровень 1)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    legal_l1_text = "Вы в разделе **2. Юридический блок**. Выберите категорию документов:"
    markup = keyboards.create_legal_menu_l1()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=legal_l1_text, reply_markup=markup, parse_mode='Markdown')

def show_docs_list_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Список документов необходимые для сделки (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Список документов необходимые для сделки**."
    markup = keyboards.create_docs_list_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_agency_agreements_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Агентские договоры (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Агентские договоры**. Выберите тип клиента:"
    markup = keyboards.create_agency_agreements_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_buyer_agreements_menu_l3(bot: TeleBot, call: types.CallbackQuery):
    """Показывает На покупателя (L3)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Агентские договоры - На покупателя**."
    markup = keyboards.create_buyer_agreements_menu_l3()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_seller_agreements_menu_l3(bot: TeleBot, call: types.CallbackQuery):
    """Показывает На продавца (L3)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Агентские договоры - На продавца**."
    markup = keyboards.create_seller_agreements_menu_l3()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_deposit_agreement_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Соглашение о задатке (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Соглашение о задатке**. Выберите нужный бланк:"
    markup = keyboards.create_deposit_agreement_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_additional_agreements_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Дополнительные соглашения к задатку (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Дополнительные соглашения к задатку**."
    markup = keyboards.create_additional_agreements_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_termination_agreement_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Соглашение о расторжении задатка (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Соглашение о расторжении задатка**. Выберите причину:"
    markup = keyboards.create_termination_agreement_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_various_docs_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Разные документы (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Разные документы**."
    markup = keyboards.create_various_docs_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_online_deposit_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Соглашение о задатке онлайн (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Соглашение о задатке онлайн**."
    markup = keyboards.create_online_deposit_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

def show_instructions_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает Инструкции, памятки и алгоритмы (L2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = "Вы в разделе **Инструкции, памятки и алгоритмы**."
    markup = keyboards.create_instructions_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')

# --- ПРОЧИЕ МЕНЮ (L1 - L2) ---

def show_score_menu(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Объекты СКОР."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    score_menu_text = "Вы в разделе **3. Объекты СКОР**. Выберите действие или перейдите в Главное меню:"
    markup = keyboards.create_score_menu()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=score_menu_text, reply_markup=markup, parse_mode='Markdown')

def show_rural_menu(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Загородная недвижимость."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    rural_menu_text = "Вы в разделе **6. Загородная недвижимость**. Выберите нужный пункт или вернитесь в Главное меню:"
    markup = keyboards.create_rural_menu()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=rural_menu_text, reply_markup=markup, parse_mode='Markdown')

def show_novice_menu_l1(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Обучение для новичков (Уровень 1)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    novice_l1_text = "Вы в разделе **1. Обучение для новичков**. Выберите тему для изучения:"
    markup = keyboards.create_novice_menu_l1()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=novice_l1_text, reply_markup=markup, parse_mode='Markdown')

def show_ries_crm_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Работа в системах РИЕС и CRM (Уровень 2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    ries_crm_text = "Вы в разделе **Работа в системах РИЕС и CRM**. Выберите инструкцию:"
    markup = keyboards.create_ries_crm_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=ries_crm_text, reply_markup=markup, parse_mode='Markdown')

def show_marketing_menu_l1(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Маркетинг (Уровень 1)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    marketing_l1_text = "Вы в разделе **7. Маркетинг**. Выберите нужный пункт:"
    markup = keyboards.create_marketing_menu_l1()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=marketing_l1_text, reply_markup=markup, parse_mode='Markdown')

def show_reviews_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Ссылки на отзывы (Уровень 2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    reviews_l2_text = "Вы в разделе **Ссылки на отзывы**. Выберите платформу:"
    markup = keyboards.create_reviews_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=reviews_l2_text, reply_markup=markup, parse_mode='Markdown')

def show_mortgage_menu_l1(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Ипотечный блок (Уровень 1)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    mortgage_l1_text = "Вы в разделе **4. Ипотечный блок**. Выберите нужный пункт:"
    markup = keyboards.create_mortgage_menu_l1()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=mortgage_l1_text, reply_markup=markup, parse_mode='Markdown')

def show_broker_training_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Обучение для ипотечного брокера (Уровень 2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    broker_l2_text = "Вы в разделе **Обучение для ипотечного брокера**. Выберите материалы:"
    markup = keyboards.create_broker_training_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=broker_l2_text, reply_markup=markup, parse_mode='Markdown')

def show_deal_map_menu_l2(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Карта сделки (Уровень 2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    deal_map_l2_text = "Вы в разделе **Карта сделки**. Выберите банк для просмотра этапов:"
    markup = keyboards.create_deal_map_menu_l2()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=deal_map_l2_text, reply_markup=markup, parse_mode='Markdown')

def show_new_buildings_menu_l1(bot: TeleBot, call: types.CallbackQuery):
    """Показывает подменю Текущие новостройки (Уровень 1)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    new_buildings_l1_text = (
        "Вы в разделе **5. Текущие новостройки**. Выберите комплекс или общую информацию:\n"
        "*(Нажмите на название ЖК, чтобы увидеть шахматку и информацию)*"
    )
    markup = keyboards.create_new_buildings_menu_l1()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_buildings_l1_text, reply_markup=markup, parse_mode='Markdown')

def show_jk_detail_menu_l2(bot: TeleBot, call: types.CallbackQuery, jk_key: str):
    """Показывает детальное меню для конкретного ЖК (Уровень 2)."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    jk_name = config.NEW_BUILDINGS_DATA.get(jk_key, {}).get("name", "Неизвестный ЖК")
    
    jk_detail_text = f"Вы выбрали **{jk_name}**. Выберите: Шахматка (наличие квартир) или Подробная информация."
    markup = keyboards.create_jk_detail_menu_l2(jk_key)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=jk_detail_text, reply_markup=markup, parse_mode='Markdown')

def show_placeholder(bot: TeleBot, call: types.CallbackQuery):
    """Отображает заглушку для нереализованных пока пунктов."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    placeholder_text = f"Этот раздел находится в разработке. Выберите **Главное меню** для продолжения."
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_main')
    )
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=placeholder_text, reply_markup=markup, parse_mode='Markdown')


# --- ОСНОВНЫЕ ОБРАБОТЧИКИ СООБЩЕНИЙ ---

def send_welcome(bot: TeleBot, message: types.Message, user_authenticated: dict):
    """Обработчик команды /start."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_authenticated[user_id] = False
    welcome_text = (
        "Вас приветствует бот V.E.R.A.! Для дальнейшей работы **введите код доступа**! "
        "Для подсказки нажмите /help"
    )
    bot.send_message(chat_id, welcome_text, parse_mode='Markdown')

def send_help(bot: TeleBot, message: types.Message):
    """Обработчик команды /help."""
    chat_id = message.chat.id
    help_text = "Код был отправлен в общем чате"
    bot.send_message(chat_id, help_text)

def send_goodbye(bot: TeleBot, message: types.Message, user_authenticated: dict):
    """Обработчик команды /stop."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_authenticated.get(user_id):
        user_authenticated[user_id] = False
        goodbye_text = "🚪 Сеанс завершен. Вы вышли из системы. Чтобы начать заново, введите /start."
    else:
        goodbye_text = "Вы уже не авторизованы. Для начала работы введите /start."
    bot.send_message(chat_id, goodbye_text)

def handle_access_code(bot: TeleBot, message: types.Message, user_authenticated: dict):
    """Обработчик ввода кода доступа."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message.text == config.ACCESS_CODE:
        user_authenticated[user_id] = True 
        show_main_menu(bot, chat_id)
    else:
        bot.send_message(chat_id, "❌ Неверный код доступа. Пожалуйста, попробуйте снова.")


# --- ОБРАБОТЧИК INLINE-КНОПОК ---

def callback_handler(bot: TeleBot, call: types.CallbackQuery, user_authenticated: dict):
    """Обрабатывает нажатия инлайн-кнопок."""
    user_id = call.from_user.id

    # Проверка аутентификации перед обработкой
    if not user_authenticated.get(user_id, False):
        bot.answer_callback_query(call.id, "Срок сессии истек. Введите /start и код доступа.", show_alert=True)
        return

    bot.answer_callback_query(call.id)
    
    # --- НАВИГАЦИЯ НАЗАД И ГЛАВНОЕ МЕНЮ ---
    if call.data == 'back_to_main':
        show_main_menu(bot, call.message.chat.id, call.message.message_id)
        
    # Назад из L2 в L1
    elif call.data == 'back_to_novice_l1': show_novice_menu_l1(bot, call)
    elif call.data == 'back_to_marketing_l1': show_marketing_menu_l1(bot, call)
    elif call.data == 'back_to_mortgage_l1': show_mortgage_menu_l1(bot, call)
    elif call.data == 'back_to_new_buildings_l1': show_new_buildings_menu_l1(bot, call)
    elif call.data == 'back_to_legal_l1': show_legal_menu_l1(bot, call)

    # Назад из L3 в L2 (только для Агентских договоров)
    elif call.data == 'back_to_agency_agreements_l2': show_agency_agreements_menu_l2(bot, call)
        
    # --- ПЕРЕХОДЫ В ПОДМЕНЮ (УРОВЕНЬ 1) ---
    elif call.data == 'menu_1': show_novice_menu_l1(bot, call)
    elif call.data == 'menu_2': show_legal_menu_l1(bot, call)
    elif call.data == 'menu_3': show_score_menu(bot, call)
    elif call.data == 'menu_4': show_mortgage_menu_l1(bot, call)
    elif call.data == 'menu_5': show_new_buildings_menu_l1(bot, call)
    elif call.data == 'menu_6': show_rural_menu(bot, call)
    elif call.data == 'menu_7': show_marketing_menu_l1(bot, call)

    # --- ПЕРЕХОДЫ В ПОДМЕНЮ (ЮР. БЛОК L2) ---
    elif call.data == 'legal_l1_docs_list': show_docs_list_menu_l2(bot, call)
    elif call.data == 'legal_l1_agency_agreements': show_agency_agreements_menu_l2(bot, call)
    elif call.data == 'legal_l1_deposit_agreement': show_deposit_agreement_menu_l2(bot, call)
    elif call.data == 'legal_l1_additional_agreements': show_additional_agreements_menu_l2(bot, call)
    elif call.data == 'legal_l1_termination_agreement': show_termination_agreement_menu_l2(bot, call)
    elif call.data == 'legal_l1_various_docs': show_various_docs_menu_l2(bot, call)
    elif call.data == 'legal_l1_online_deposit': show_online_deposit_menu_l2(bot, call)
    elif call.data == 'legal_l1_instructions': show_instructions_menu_l2(bot, call)
        
    # --- ПЕРЕХОДЫ В ПОДМЕНЮ (ЮР. БЛОК L3) ---
    elif call.data == 'legal_l2_for_buyer': show_buyer_agreements_menu_l3(bot, call)
    elif call.data == 'legal_l2_for_seller': show_seller_agreements_menu_l3(bot, call)

    # --- ПЕРЕХОДЫ В ОСТАЛЬНЫЕ ПОДМЕНЮ (L2) ---
    elif call.data == 'novice_l1_ries': show_ries_crm_menu_l2(bot, call)
    elif call.data == 'marketing_l1_reviews': show_reviews_menu_l2(bot, call)
    elif call.data == 'mortgage_l1_broker_training': show_broker_training_menu_l2(bot, call)
    elif call.data == 'mortgage_l1_deal_map': show_deal_map_menu_l2(bot, call)
    elif call.data.startswith('jk_detail_'):
        jk_key = call.data.replace('jk_detail_', '')
        show_jk_detail_menu_l2(bot, call, jk_key)
        
    # --- Игнор разделителя ---
    elif call.data == 'ignore_separator':
        pass