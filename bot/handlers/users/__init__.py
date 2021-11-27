from states.state import SetSearchName, SetSearchKeyword
from . import common, search

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.search import cd_search, cd_checkbox


def register_handlers_common(dp: Dispatcher):
    """Register common handlers in Dispatcher."""
    dp.register_message_handler(common.cmd_start, commands='start')
    #dp.register_message_handler(common.cmd_cancel, commands='cancel', state='*')


def register_handlers_search(dp: Dispatcher):
    """Register routes handlers in Dispatcher."""

    dp.register_message_handler(search.search_main, commands='search')
    dp.register_callback_query_handler(search.search_main, cd_search.filter(action='main'))
    dp.register_callback_query_handler(search.search_list, cd_search.filter(action='list'))

    dp.register_callback_query_handler(search.search_category_list, cd_search.filter(action='category'))
    dp.register_callback_query_handler(search.search_country_list, cd_search.filter(action='country'))
    dp.register_callback_query_handler(search.search_language_list, cd_search.filter(action='language'))
    dp.register_callback_query_handler(search.search_topic_list, cd_search.filter(action='topic'))

    dp.register_callback_query_handler(search.search_subs_list, cd_search.filter(action='subs'))
    dp.register_callback_query_handler(search.search_views_list, cd_search.filter(action='views'))
    dp.register_callback_query_handler(search.search_videos_list, cd_search.filter(action='videos'))

    dp.register_callback_query_handler(search.search_latest_list, cd_search.filter(action='latest'))
    dp.register_callback_query_handler(search.search_creation_list, cd_search.filter(action='creation'))

    dp.register_callback_query_handler(search.start_search, cd_search.filter(action='start'))
    dp.register_callback_query_handler(search.do_search, cd_search.filter(action='do-search'))


    #UPDATE CHECKBOX
    dp.register_callback_query_handler(search.update_category, cd_checkbox.filter(action='update-category'))
    dp.register_callback_query_handler(search.update_country, cd_checkbox.filter(action='update-country'))
    dp.register_callback_query_handler(search.update_language, cd_checkbox.filter(action='update-language'))
    dp.register_callback_query_handler(search.update_topic, cd_checkbox.filter(action='update-topic'))

    #PAGING CHECKBOX
    dp.register_callback_query_handler(search.page_category, cd_checkbox.filter(action='page-category'))
    dp.register_callback_query_handler(search.page_country, cd_checkbox.filter(action='page-country'))
    dp.register_callback_query_handler(search.page_language, cd_checkbox.filter(action='page-language'))
    dp.register_callback_query_handler(search.page_topic, cd_checkbox.filter(action='page-topic'))

    #MIN-MAX SELECT
    dp.register_callback_query_handler(search.select_min_subs, cd_search.filter(action='select-min-subs'))
    dp.register_callback_query_handler(search.select_max_subs, cd_search.filter(action='select-max-subs'))
    dp.register_callback_query_handler(search.select_min_views, cd_search.filter(action='select-min-views'))
    dp.register_callback_query_handler(search.select_max_views, cd_search.filter(action='select-max-views'))
    dp.register_callback_query_handler(search.select_min_videos, cd_search.filter(action='select-min-videos'))
    dp.register_callback_query_handler(search.select_max_videos, cd_search.filter(action='select-max-videos'))

    dp.register_callback_query_handler(search.select_min_latest, cd_search.filter(action='select-min-latest'))
    dp.register_callback_query_handler(search.select_max_latest, cd_search.filter(action='select-max-latest'))
    dp.register_callback_query_handler(search.select_min_creation, cd_search.filter(action='select-min-creation'))
    dp.register_callback_query_handler(search.select_max_creation, cd_search.filter(action='select-max-creation'))


    #INPUTS
    dp.register_callback_query_handler(search.search_name_change, cd_search.filter(action='name-change'))
    dp.register_callback_query_handler(search.search_keyword_change, cd_search.filter(action='keyword-change'))

    dp.register_message_handler(search.search_input_set)