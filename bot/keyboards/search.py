from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    inline_keyboard
)
from aiogram.utils.callback_data import CallbackData
from aiogram import types

from utils import uchar

cd_search = CallbackData('search_menu', 'action', 'data')
cd_checkbox = CallbackData('category_menu', 'action', 'id', 'status', 'item_id', 'page')

cb_cancel = cd_search.new(action='cancel', data='void')
btn_cancel = InlineKeyboardButton('Cancel', callback_data=cb_cancel)


def kb_search_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                        'Start search',
                        callback_data=cd_search.new(action='list', data=False),
                    )
            ]
        ]
    )


def kb_search() -> InlineKeyboardMarkup:
    """Return keyboard with list of search."""
    inline_search = InlineKeyboardMarkup(row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    'Input channel name',
                    callback_data=cd_search.new(action='name-change', data=False),
                ),

                InlineKeyboardButton(
                    'Input keywords',
                    callback_data=cd_search.new(action='keyword-change', data=False),
                )     
            ],
        ]
    )

    inline_search.row(
        InlineKeyboardButton(
            'Select topic',
            callback_data=cd_search.new(action='topic', data=False),
        ),

        InlineKeyboardButton(
            'Select category',
            callback_data=cd_search.new(action='category', data=False),
        )
    )

    inline_search.row(
        InlineKeyboardButton(
            'Select language',
            callback_data=cd_search.new(action='language', data=False),
        ),

        InlineKeyboardButton(
            'Select country',
            callback_data=cd_search.new(action='country', data=False),
        )
    )

    inline_search.row(
        InlineKeyboardButton(
            'Select total views count',
            callback_data=cd_search.new(action='views', data=False),
        ),

        InlineKeyboardButton(
            'Select subscribes count',
            callback_data=cd_search.new(action='subs', data=False),
        )
    )

    inline_search.row(
        InlineKeyboardButton(
            'Select latest video date',
            callback_data=cd_search.new(action='latest', data=False),
        ),

        InlineKeyboardButton(
            'Select creation date',
            callback_data=cd_search.new(action='creation', data=False),
        )
    )

    inline_search.row(
        InlineKeyboardButton(
            'Select total video count',
            callback_data=cd_search.new(action='videos', data=False),
        )
    )

    inline_search.add(
        InlineKeyboardButton(
                    'Start search',
                    callback_data=cd_search.new(action='start', data=False),
            )
    )


    return inline_search


def kb_search_checkbox(checkboxs, action_menu, page = 0, per_page = 8) -> InlineKeyboardMarkup:

    checkbox_button = []
    list_chkbox = [checkboxs[i:i+per_page] for i in range(0, len(checkboxs), per_page)]
    has_next_page = len(list_chkbox) > int(page) + 1

    for i in list_chkbox[int(page)]:
        chbox_name = i[1]
        if i[2] == '0':
            check_status = uchar.CROSS_MARK
        else:
            check_status = uchar.CHECK_MARK
        checkbox_button.append(
            InlineKeyboardButton(f'{check_status} {chbox_name}', 
                                        callback_data=cd_checkbox.new(action=f'update-{action_menu}', id=str(i[0]), status=str(i[2]), item_id=str(i[3]), page=page) 
            ))

    
    paging_btn = []
    if int(page) != 0:
        paging_btn.append(InlineKeyboardButton(
            'Previous page',
            callback_data=cd_checkbox.new(action=f'page-{action_menu}', id=False, status=False, item_id=False, page=int(page)-1 )
        ))
    
    if has_next_page:
        paging_btn.append(InlineKeyboardButton(
            'Next page',
            callback_data=cd_checkbox.new(action=f'page-{action_menu}', id=False, status=False, item_id=False, page=int(page)+1)
        ))

    chboxer_kb = InlineKeyboardMarkup(row_width=2)
    chboxer_kb.add(*checkbox_button)
    chboxer_kb.add(*paging_btn)

    chboxer_kb.add(InlineKeyboardButton(
                    f'{uchar.BACK_ARROW} Back',
                    callback_data=cd_search.new(action='list', data=False),
                ))

    return chboxer_kb


def kb_search_min_max(nums, action_menu) -> InlineKeyboardMarkup:
    nums_button = []

    for i in range (0, len(nums["name"])):
        num_name = nums["name"][i]
        num_data = nums["data"][i]
        nums_button.append(
            InlineKeyboardButton(f'{num_name}', callback_data=cd_search.new(action=f'select-{action_menu}', data=num_data) 
            ))

    nums_kb = InlineKeyboardMarkup(row_width=2)
    nums_kb.add(*nums_button)
    nums_kb.add(InlineKeyboardButton(
                    f'{uchar.BACK_ARROW} Back',
                    callback_data=cd_search.new(action='list', data=False),
                ))
    
    return nums_kb


def kb_search_yesno() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    'Yes',
                    callback_data=cd_search.new(action='do-search', data=False),
                ),

                InlineKeyboardButton(
                    f'{uchar.BACK_ARROW} Back',
                    callback_data=cd_search.new(action='list', data=False),
                )
            ],
        ]
    )

def kb_search_back() -> InlineKeyboardMarkup:
    """Keyboard for get user back to list of search."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    f'{uchar.BACK_ARROW} Back',
                    callback_data=cd_search.new(action='list', data=False),
                )
            ],
        ]
    )


                

                