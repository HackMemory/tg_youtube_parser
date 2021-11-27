# -*- coding: utf-8 -*-

import asyncio
from time import sleep
from typing import Union
from aiogram import types
from utils import uchar
from time import gmtime, strftime

from loader import dp
from youtube import YouTube
from keyboards import search
from states.state import SetSearchKeyword, SetSearchName
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.webhook import DeleteMessage
from aiogram.dispatcher.filters import Text

async def search_main(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    caption = 'Set up filters and start searching'
    kb = search.kb_search_main()

    await state.set_data({
        "name": "",
        "keyword": "",
        "min_subs": "",
        "max_subs": "",
        "min_views": "",
        "max_views": "",
        "min_videos": "",
        "max_videos": "",
        "min_latest": "",
        "max_latest": "",
        "min_creation": "",
        "max_creation": "",
        "current_page": 0,
        "category": [
            [0, "Autos & Vehicles", '0', '2'],
            [1, "Comedy", '0', '23'],
            [2, "Education", '0', '27'],
            [3, "Entertainment", '0', '24'],
            [4, "Film and Animation", '0', '1'],
            [5, "Gaming", '0', '20'],
            [6, "Howto & Style", '0', '26'],
            [7, "Music", '0', '10'],
            [8, "News & Politics", '0', '25'],
            [9, "Nonprofits & Activism", '0', '29'],
            [10, "People & Blogs", '0', '22'],
            [11, "Pets & Animals", '0', '15'],
            [12, "Science & Technology", '0', '28'],
            [13, "Sports", '0', '17'],
            [14, "Travel & Events", '0', '19']
        ],
        "country": [
                ["0", "Russian Federation", "0", "492"],
                ["1", "Ukraine", "0", "541"],
                ["2", "Belarus", "0", "330"],
                ["3", "United States", "0", "2"],
                ["4", "United Kingdom", "0", "1"],
                ["5", "Canada", "0", "3"],
                ["6", "Australia", "0", "4"],
                ["7", "Afghanistan", "0", "310"],
                ["8", "Aland Islands", "0", "311"],
                ["9", "Albania", "0", "312"],
                ["10", "Algeria", "0", "313"],
                ["11", "American Samoa", "0", "15"],
                ["12", "Andorra", "0", "315"],
                ["13", "Angola", "0", "316"],
                ["14", "Anguilla", "0", "21"],
                ["15", "Antarctica", "0", "318"],
                ["16", "Antigua & Barbuda", "0", "25"],
                ["17", "Argentina", "0", "45"],
                ["18", "Armenia", "0", "321"],
                ["19", "Aruba", "0", "35"],
                ["20", "Austria", "0", "39"],
                ["21", "Azerbaijan", "0", "325"],
                ["22", "Bahamas", "0", "11"],
                ["23", "Bahrain", "0", "327"],
                ["24", "Bangladesh", "0", "328"],
                ["25", "Barbados", "0", "17"],
                ["26", "BelgiГ«", "0", "30"],
                ["27", "Belize", "0", "332"],
                ["28", "Benin", "0", "333"],
                ["29", "Bermuda", "0", "18"],
                ["30", "Bhutan", "0", "335"],
                ["31", "Bolivia", "0", "52"],
                ["32", "Bosnia and Herzegovina", "0", "337"],
                ["33", "Botswana", "0", "338"],
                ["34", "Bouvet Island", "0", "339"],
                ["35", "Brazil", "0", "340"],
                ["36", "British Indian Ocean Territory", "0", "14"],
                ["37", "Brunei Darussalam", "0", "343"],
                ["38", "Bulgaria", "0", "344"],
                ["39", "Burkina Faso", "0", "345"],
                ["40", "Burundi", "0", "346"],
                ["41", "Cambodia", "0", "347"],
                ["42", "Cameroon", "0", "348"],
                ["43", "Cape Verde", "0", "350"],
                ["44", "Cayman Islands", "0", "27"],
                ["45", "Central African Republic", "0", "352"],
                ["46", "Chad", "0", "353"],
                ["47", "Chile", "0", "48"],
                ["48", "China", "0", "355"],
                ["49", "Christmas Island", "0", "358"],
                ["50", "Cocos (Keeling) Islands", "0", "359"],
                ["51", "Colombia", "0", "44"],
                ["52", "Comoros", "0", "361"],
                ["53", "Congo (Brazzaville)", "0", "362"],
                ["54", "Congo, Democratic Republic of the", "0", "363"],
                ["55", "Cook Islands", "0", "364"],
                ["56", "Costa Rica", "0", "58"],
                ["57", "Croatia", "0", "367"],
                ["58", "Cuba", "0", "51"],
                ["59", "Curacao", "0", "31"],
                ["60", "Cyprus", "0", "369"],
                ["61", "Czech Republic", "0", "370"],
                ["62", "Denmark", "0", "371"],
                ["63", "Djibouti", "0", "372"],
                ["64", "Dominica", "0", "373"],
                ["65", "Dominican Republic", "0", "53"],
                ["66", "Ecuador", "0", "49"],
                ["67", "Egypt", "0", "376"],
                ["68", "El Salvador", "0", "56"],
                ["69", "Equatorial Guinea", "0", "62"],
                ["70", "Eritrea", "0", "379"],
                ["71", "Estonia", "0", "380"],
                ["72", "Ethiopia", "0", "381"],
                ["73", "Falkland Islands", "0", "20"],
                ["74", "Faroe Islands", "0", "383"],
                ["75", "Fiji", "0", "384"],
                ["76", "Finland", "0", "41"],
                ["77", "France", "0", "386"],
                ["78", "French Guiana", "0", "387"],
                ["79", "French Polynesia", "0", "388"],
                ["80", "French Southern Territories", "0", "389"],
                ["81", "Gabon", "0", "390"],
                ["82", "Gambia", "0", "391"],
                ["83", "Georgia", "0", "392"],
                ["84", "Germany", "0", "37"],
                ["85", "Ghana", "0", "394"],
                ["86", "Gibraltar", "0", "395"],
                ["87", "Greece", "0", "396"],
                ["88", "Greenland", "0", "397"],
                ["89", "Grenada", "0", "13"],
                ["90", "Guadeloupe", "0", "399"],
                ["91", "Guam", "0", "400"],
                ["92", "Guatemala", "0", "50"],
                ["93", "Guernsey", "0", "402"],
                ["94", "Guinea", "0", "403"],
                ["95", "Guinea-Bissau", "0", "404"],
                ["96", "Guyana", "0", "10"],
                ["97", "Haiti", "0", "406"],
                ["98", "Heard Island and Mcdonald Islands", "0", "407"],
                ["99", "Holy See (Vatican City State)", "0", "408"],
                ["100", "Honduras", "0", "54"],
                ["101", "Hong Kong, Special Administrative Region of China", "0", "356"],
                ["102", "Hungary", "0", "410"],
                ["103", "Iceland", "0", "411"],
                ["104", "India", "0", "99"],
                ["105", "Indonesia", "0", "413"],
                ["106", "Iran, Islamic Republic of", "0", "414"],
                ["107", "Iraq", "0", "415"],
                ["108", "Ireland", "0", "6"],
                ["109", "Isle of Man", "0", "16"],
                ["110", "Israel", "0", "418"],
                ["111", "Italy", "0", "419"],
                ["112", "Ivory Coast", "0", "366"],
                ["113", "Jamaica", "0", "8"],
                ["114", "Japan", "0", "421"],
                ["115", "Jersey", "0", "422"],
                ["116", "Jordan", "0", "423"],
                ["117", "Kazakhstan", "0", "424"],
                ["118", "Kenya", "0", "425"],
                ["119", "Kiribati", "0", "426"],
                ["120", "Korea, Democratic People's Republic of", "0", "427"],
                ["121", "Korea, Republic of", "0", "428"],
                ["122", "Kosovo", "0", "557"],
                ["123", "Kuwait", "0", "429"],
                ["124", "Kyrgyzstan", "0", "430"],
                ["125", "Lao PDR", "0", "431"],
                ["126", "Latvia", "0", "432"],
                ["127", "Lebanon", "0", "433"],
                ["128", "Lesotho", "0", "434"],
                ["129", "Liberia", "0", "435"],
                ["130", "Libya", "0", "436"],
                ["131", "Liechtenstein", "0", "36"],
                ["132", "Lithuania", "0", "438"],
                ["133", "Luxembourg", "0", "40"],
                ["134", "Macao, Special Administrative Region of China", "0", "357"],
                ["135", "Madagascar", "0", "441"],
                ["136", "Malawi", "0", "442"],
                ["137", "Malaysia", "0", "443"],
                ["138", "Maldives", "0", "444"],
                ["139", "Mali", "0", "445"],
                ["140", "Malta", "0", "446"],
                ["141", "Marshall Islands", "0", "447"],
                ["142", "Martinique", "0", "448"],
                ["143", "Mauritania", "0", "449"],
                ["144", "Mauritius", "0", "450"],
                ["145", "Mayotte", "0", "451"],
                ["146", "Mexico", "0", "43"],
                ["147", "Micronesia, Federated States of", "0", "453"],
                ["148", "Moldova", "0", "454"],
                ["149", "Monaco", "0", "455"],
                ["150", "Mongolia", "0", "456"],
                ["151", "Montenegro", "0", "457"],
                ["152", "Montserrat", "0", "28"],
                ["153", "Morocco", "0", "459"],
                ["154", "Mozambique", "0", "460"],
                ["155", "Myanmar", "0", "461"],
                ["156", "Namibia", "0", "462"],
                ["157", "Nauru", "0", "463"],
                ["158", "Nederland", "0", "29"],
                ["159", "Nederlandse Antillen", "0", "33"],
                ["160", "Nepal", "0", "464"],
                ["161", "New Caledonia", "0", "467"],
                ["162", "New-Zealand", "0", "5"],
                ["163", "Nicaragua", "0", "57"],
                ["164", "Niger", "0", "470"],
                ["165", "Nigeria", "0", "471"],
                ["166", "Niue", "0", "472"],
                ["167", "Norfolk Island", "0", "473"],
                ["168", "North-Macedonia", "0", "440"],
                ["169", "Northern Mariana Islands", "0", "474"],
                ["170", "Norway", "0", "475"],
                ["171", "Oman", "0", "476"],
                ["172", "Pakistan", "0", "477"],
                ["173", "Palau", "0", "478"],
                ["174", "Palestinian Territory, Occupied", "0", "479"],
                ["175", "Panama", "0", "60"],
                ["176", "Papua New Guinea", "0", "481"],
                ["177", "Paraguay", "0", "55"],
                ["178", "Peru", "0", "46"],
                ["179", "Philippines", "0", "484"],
                ["180", "Pitcairn", "0", "22"],
                ["181", "Poland", "0", "486"],
                ["182", "Portugal", "0", "487"],
                ["183", "Puerto Rico", "0", "59"],
                ["184", "Qatar", "0", "489"],
                ["185", "RГ©union", "0", "490"],
                ["186", "Romania", "0", "491"],
                ["187", "Rwanda", "0", "493"],
                ["188", "Saint Helena, Ascension & Tristan da Cunha", "0", "24"],
                ["189", "Saint Kitts & Nevis", "0", "26"],
                ["190", "Saint Lucia", "0", "497"],
                ["191", "Saint Pierre and Miquelon", "0", "499"],
                ["192", "Saint Vincent & The Grenadines", "0", "12"],
                ["193", "Saint-Barth", "0", "494"],
                ["194", "Saint-Martin (French part)", "0", "498"],
                ["195", "Samoa", "0", "501"],
                ["196", "San Marino", "0", "502"],
                ["197", "Sao Tome and Principe", "0", "503"],
                ["198", "Saudi Arabia", "0", "504"],
                ["199", "Senegal", "0", "505"],
                ["200", "Serbia", "0", "506"],
                ["201", "Seychelles", "0", "507"],
                ["202", "Sierra Leone", "0", "508"],
                ["203", "Singapore", "0", "509"],
                ["204", "Sint-Maarten", "0", "34"],
                ["205", "Slovakia", "0", "510"],
                ["206", "Slovenia", "0", "511"],
                ["207", "Solomon Islands", "0", "512"],
                ["208", "Somalia", "0", "513"],
                ["209", "South Georgia and the South Sandwich Islands", "0", "515"],
                ["210", "South Sudan", "0", "516"],
                ["211", "South-Africa", "0", "7"],
                ["212", "Spain", "0", "42"],
                ["213", "Sri Lanka", "0", "518"],
                ["214", "Sudan", "0", "519"],
                ["215", "Suriname", "0", "32"],
                ["216", "Svalbard and Jan Mayen Islands", "0", "521"],
                ["217", "Swaziland", "0", "522"],
                ["218", "Sweden", "0", "523"],
                ["219", "Switzerland", "0", "38"],
                ["220", "Syrian Arab Republic (Syria)", "0", "525"],
                ["221", "Taiwan, Republic of China", "0", "526"],
                ["222", "Tajikistan", "0", "527"],
                ["223", "Tanzania", "0", "528"],
                ["224", "Thailand", "0", "529"],
                ["225", "Timor-Leste", "0", "530"],
                ["226", "Togo", "0", "531"],
                ["227", "Tokelau", "0", "532"],
                ["228", "Tonga", "0", "533"],
                ["229", "Trinidad & Tobago", "0", "9"],
                ["230", "Tunisia", "0", "535"],
                ["231", "Turkey", "0", "536"],
                ["232", "Turkmenistan", "0", "537"],
                ["233", "Turks and Caicos Islands", "0", "538"],
                ["234", "Tuvalu", "0", "539"],
                ["235", "Uganda", "0", "540"],
                ["236", "United Arab Emirates", "0", "542"],
                ["237", "United States Minor Outlying Islands", "0", "545"],
                ["238", "Uruguay", "0", "61"],
                ["239", "Uzbekistan", "0", "547"],
                ["240", "Vanuatu", "0", "548"],
                ["241", "Venezuela", "0", "47"],
                ["242", "Viet Nam", "0", "550"],
                ["243", "Virgin Islands, British", "0", "23"],
                ["244", "Virgin Islands, U.S.", "0", "19"],
                ["245", "Wallis and Futuna Islands", "0", "552"],
                ["246", "Western Sahara", "0", "553"],
                ["247", "Yemen", "0", "554"],
                ["248", "Zambia", "0", "555"],
                ["249", "Zimbabwe", "0", "556"],
        ],
        "language": [
                ["0", "Russian", "0", "15"],
                ["1", "Ukrainian", "0", "137"],
                ["2", "Belarusian", "0", "27"],
                ["3", "English", "0", "7"],
                ["4", "Abkhazian", "0", "382"],
                ["5", "Afar", "0", "381"],
                ["6", "Afrikaans", "0", "105"],
                ["7", "Akan", "0", "383"],
                ["8", "Albanian", "0", "9"],
                ["9", "Amharic", "0", "58"],
                ["10", "Arabic", "0", "11"],
                ["11", "Armenian", "0", "14"],
                ["12", "Assamese", "0", "384"],
                ["13", "Aymara", "0", "29"],
                ["14", "Azerbaijani", "0", "19"],
                ["15", "Bashkir", "0", "385"],
                ["16", "Basque", "0", "54"],
                ["17", "Bengali", "0", "22"],
                ["18", "Bihari", "0", "386"],
                ["19", "Bislama", "0", "141"],
                ["20", "Bosnian", "0", "24"],
                ["21", "Breton", "0", "388"],
                ["22", "Buginese", "0", "389"],
                ["23", "Bulgarian", "0", "23"],
                ["24", "Burmese", "0", "100"],
                ["25", "Catalan", "0", "10"],
                ["26", "Cebuano", "0", "390"],
                ["27", "Cherokee", "0", "391"],
                ["28", "Chinese Simplified", "0", "449"],
                ["29", "Chinese Traditional", "0", "450"],
                ["30", "Corsican", "0", "392"],
                ["31", "Croatian", "0", "25"],
                ["32", "Czech", "0", "48"],
                ["33", "Danish", "0", "50"],
                ["34", "Dhivehi", "0", "395"],
                ["35", "Dutch", "0", "1"],
                ["36", "Dzongkha", "0", "32"],
                ["37", "Egyptian", "0", "396"],
                ["38", "Esperanto", "0", "397"],
                ["39", "Estonian", "0", "57"],
                ["40", "Faroese", "0", "62"],
                ["41", "Fijian", "0", "60"],
                ["42", "Finnish", "0", "59"],
                ["43", "French", "0", "17"],
                ["44", "Frisian", "0", "398"],
                ["45", "Galician", "0", "55"],
                ["46", "Ganda", "0", "416"],
                ["47", "Georgian", "0", "63"],
                ["48", "German", "0", "21"],
                ["49", "Gothic", "0", "401"],
                ["50", "Greek", "0", "46"],
                ["51", "Greenlandic", "0", "65"],
                ["52", "Guarani", "0", "400"],
                ["53", "Gujarati", "0", "402"],
                ["54", "Haitian Creole", "0", "67"],
                ["55", "Hausa", "0", "403"],
                ["56", "Hawaiian", "0", "404"],
                ["57", "Hebrew", "0", "78"],
                ["58", "Hindi", "0", "71"],
                ["59", "Hmong", "0", "405"],
                ["60", "Hungarian", "0", "68"],
                ["61", "Icelandic", "0", "77"],
                ["62", "Igbo", "0", "408"],
                ["63", "Indonesian", "0", "69"],
                ["64", "Interlingua", "0", "406"],
                ["65", "Interlingue", "0", "407"],
                ["66", "Inuktitut", "0", "410"],
                ["67", "Inupiak", "0", "409"],
                ["68", "Irish", "0", "73"],
                ["69", "Italian", "0", "37"],
                ["70", "Japanese", "0", "82"],
                ["71", "Javanese", "0", "411"],
                ["72", "Kannada", "0", "413"],
                ["73", "Kashmiri", "0", "414"],
                ["74", "Kazakh", "0", "83"],
                ["75", "Khasi", "0", "412"],
                ["76", "Khmer", "0", "85"],
                ["77", "Kinyarwanda", "0", "126"],
                ["78", "Klingon", "0", "440"],
                ["79", "Korean", "0", "87"],
                ["80", "Kurdish", "0", "415"],
                ["81", "Kyrgyz", "0", "84"],
                ["82", "Laothian", "0", "418"],
                ["83", "Latin", "0", "139"],
                ["84", "Latvian", "0", "93"],
                ["85", "Limbu", "0", "417"],
                ["86", "Lingala", "0", "41"],
                ["87", "Lithuanian", "0", "91"],
                ["88", "Luxembourgish", "0", "92"],
                ["89", "Macedonian", "0", "98"],
                ["90", "Malagasy", "0", "95"],
                ["91", "Malay", "0", "31"],
                ["92", "Malayalam", "0", "419"],
                ["93", "Maltese", "0", "99"],
                ["94", "Manx", "0", "70"],
                ["95", "Maori", "0", "118"],
                ["96", "Marathi", "0", "420"],
                ["97", "Mauritian Creole", "0", "103"],
                ["98", "Mongolian", "0", "101"],
                ["99", "Nauru", "0", "117"],
                ["100", "Ndebele", "0", "421"],
                ["101", "Nepali", "0", "116"],
                ["102", "Norwegian", "0", "33"],
                ["103", "Nyanja", "0", "423"],
                ["104", "Occitan", "0", "56"],
                ["105", "Oriya", "0", "425"],
                ["106", "Oromo", "0", "424"],
                ["107", "Pashto", "0", "4"],
                ["108", "Pedi", "0", "422"],
                ["109", "Persian", "0", "74"],
                ["110", "Polish", "0", "125"],
                ["111", "Portuguese", "0", "6"],
                ["112", "Punjabi", "0", "426"],
                ["113", "Quechua", "0", "30"],
                ["114", "Rhaeto Romance", "0", "427"],
                ["115", "Romanian", "0", "94"],
                ["116", "Rundi", "0", "428"],
                ["117", "Samoan", "0", "16"],
                ["118", "Sango", "0", "35"],
                ["119", "Sanskrit", "0", "429"],
                ["120", "Scots", "0", "430"],
                ["121", "Scots Gaelic", "0", "399"],
                ["122", "Serbian", "0", "26"],
                ["123", "Seselwa", "0", "393"],
                ["124", "Sesotho", "0", "435"],
                ["125", "Shona", "0", "153"],
                ["126", "Sindhi", "0", "431"],
                ["127", "Sinhalese", "0", "432"],
                ["128", "Siswant", "0", "434"],
                ["129", "Slovak", "0", "49"],
                ["130", "Slovenian", "0", "433"],
                ["131", "Somali", "0", "127"],
                ["132", "Spanish", "0", "13"],
                ["133", "Sundanese", "0", "436"],
                ["134", "Swahili", "0", "43"],
                ["135", "Swedish", "0", "8"],
                ["136", "Syriac", "0", "437"],
                ["137", "Tagalog", "0", "439"],
                ["138", "Tajik", "0", "132"],
                ["139", "Tamil", "0", "72"],
                ["140", "Tatar", "0", "441"],
                ["141", "Telugu", "0", "438"],
                ["142", "Thai", "0", "131"],
                ["143", "Tibetan", "0", "387"],
                ["144", "Tigrinya", "0", "51"],
                ["145", "Tonga", "0", "154"],
                ["146", "Tsonga", "0", "144"],
                ["147", "Tswana", "0", "34"],
                ["148", "Turkish", "0", "47"],
                ["149", "Turkmen", "0", "5"],
                ["150", "Uighur", "0", "442"],
                ["151", "Urdu", "0", "120"],
                ["152", "Uzbek", "0", "138"],
                ["153", "Venda", "0", "145"],
                ["154", "Vietnamese", "0", "140"],
                ["155", "Volapuk", "0", "443"],
                ["156", "Waray Philippines", "0", "444"],
                ["157", "Welsh", "0", "394"],
                ["158", "Wolof", "0", "445"],
                ["159", "Xhosa", "0", "146"],
                ["160", "Yiddish", "0", "446"],
                ["161", "Yoruba", "0", "447"],
                ["162", "Zhuang", "0", "448"],
                ["163", "Zulu", "0", "147"],
        ],
        "topic": [
            [0, "Action game", '0', '1'],
            [1, "Action-adventure game", '0', '29'],
            [2, "American football", '0', '8'],
            [3, "Association football", '0', '44'],
            [4, "Baseball", '0', '68'],
            [5, "Basketball", '0', '50'],
            [6, "Boxing", '0', '59'],
            [7, "Business", '0', '69'],
            [8, "Casual game", '0', '56'],
            [9, "Christian music", '0', '52'],
            [10, "Classical music", '0', '34'],
            [11, "Country music", '0', '31'],
            [12, "Cricket", '0', '58'],
            [13, "Electronic music", '0', '15'],
            [14, "Entertainment", '0', '4'],
            [15, "Fashion", '0', '39'],
            [16, "Film", '0', '13'],
            [17, "Food", '0', '5'],
            [18, "Golf", '0', '65'],
            [19, "Health", '0', '11'],
            [20, "Hip hop music", '0', '7'],
            [21, "Hobby", '0', '24'],
            [22, "Humour", '0', '53'],
            [23, "Ice hockey", '0', '66'],
            [24, "Independent music", '0', '35'],
            [25, "Jazz", '0', '64'],
            [26, "Knowledge", '0', '12'],
            [27, "Lifestyle (sociology)", '0', '10'],
            [28, "Military", '0', '63'],
            [29, "Mixed martial arts", '0', '62'],
            [30, "Motorsport", '0', '54'],
            [31, "Music", '0', '9'],
            [32, "Music of Asia", '0', '51'],
            [33, "Music of Latin America", '0', '48'],
            [34, "Music video game", '0', '61'],
            [35, "Performing arts", '0', '33'],
            [36, "Pet", '0', '37'],
            [37, "Physical attractiveness", '0', '70'],
            [38, "Physical fitness", '0', '46'],
            [39, "Politics", '0', '42'],
            [40, "Pop music", '0', '30'],
            [41, "Professional wrestling", '0', '55'],
            [42, "Puzzle video game", '0', '57'],
            [43, "Racing video game", '0', '41'],
            [44, "Reggae", '0', '60'],
            [45, "Religion", '0', '43'],
            [46, "Rhythm and blues", '0', '47'],
            [47, "Rock music", '0', '32'],
            [48, "Role-playing video game", '0', '14'],
            [49, "Simulation video game", '0', '26'],
            [50, "Society", '0', '27'],
            [51, "Soul music", '0', '48'],
            [52, "Sport", '0', '6'],
            [53, "Sports game", '0', '2'],
            [54, "Strategy video game", '0', '28'],
            [55, "Technology", '0', '25'],
            [56, "Television program", '0', '40'],
            [57, "Tennis", '0', '67'],
            [58, "Tourism", '0', '38'],
            [59, "Vehicle", '0', '36'],
            [60, "Video game culture", '0', '3'],
            [61, "Volleyball", '0', '45'],
        ],
    })


    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def search_list(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    """Display list of all search settings."""
    caption = 'Select search filters:'
    kb = search.kb_search()

    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def search_name_change(cb: types.CallbackQuery, state: FSMContext):
    """Write the name of the channel"""

    await state.update_data(name="$current$")
    await cb.message.edit_text(
        'Write the name of the channel',
        reply_markup=None,
        disable_web_page_preview=True,
    )

async def search_keyword_change(cb: types.CallbackQuery, state: FSMContext):
    """Write the keywords"""
    await state.update_data(keyword="$current$")
    await cb.message.edit_text(
        'Write keywords\n'
        '<i>(Tip: enter i.e. <b>-minecraft</b> to exclude Minecraft data from your search)</i>',
        reply_markup=None,
        disable_web_page_preview=True,
    )

async def search_input_set(message: types.Message, state: FSMContext):
    msg = message.text
    data = await state.get_data()
    if data["name"] == "$current$": await state.update_data(name=msg)
    if data["keyword"] == "$current$": await state.update_data(keyword=msg)

    await message.answer(
        f'You wrote: {msg}',
        reply_markup=search.kb_search_back(),
    )



##############
###CATEGORY###
##############

async def search_category_list(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    """Display list of all search category."""
    caption = 'Select category:'
    data = await state.get_data()
    await state.update_data(current_page="0")

    kb = search.kb_search_checkbox(data['category'], 'category')
    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def update_category(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data_id = callback_data['id']
    data_status = callback_data['status']
    
    data = await state.get_data()
    data['category'][int(data_id)][2] = '1' if data_status == '0' else '0'

    await state.update_data(data)
    kb = search.kb_search_checkbox(data['category'], 'category', data["current_page"])
    await call.message.edit_reply_markup(reply_markup=kb)
    await call.answer(cache_time=2)

async def page_category(entity: Union[types.Message, types.CallbackQuery], callback_data: dict, state: FSMContext):
    page = callback_data['page']
    data = await state.get_data()

    await state.update_data(current_page=page)
    kb = search.kb_search_checkbox(data['category'], 'category', page)
    await entity.message.edit_reply_markup(reply_markup=kb)
    await entity.answer()


#############
###COUNTRY###
#############

async def search_country_list(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    """Display list of all search country."""
    caption = 'Select country:'
    data = await state.get_data()
    await state.update_data(current_page="0")

    kb = search.kb_search_checkbox(data['country'], 'country')
    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def update_country(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data_id = callback_data['id']
    data_status = callback_data['status']
    
    data = await state.get_data()
    data['country'][int(data_id)][2] = '1' if data_status == '0' else '0'

    await state.update_data(data)
    kb = search.kb_search_checkbox(data['country'], 'country', data["current_page"])
    await call.message.edit_reply_markup(reply_markup=kb)
    await call.answer()

async def page_country(entity: Union[types.Message, types.CallbackQuery], callback_data: dict, state: FSMContext):
    page = callback_data['page']
    data = await state.get_data()

    await state.update_data(current_page=page)
    kb = search.kb_search_checkbox(data['country'], 'country', page)
    await entity.message.edit_reply_markup(reply_markup=kb)
    await entity.answer()


###############
###LANGUAGES###
###############

async def search_language_list(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    """Display list of all search language."""
    caption = 'Select language:'
    data = await state.get_data()
    await state.update_data(current_page="0")

    kb = search.kb_search_checkbox(data['language'], 'language')
    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def update_language(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data_id = callback_data['id']
    data_status = callback_data['status']
    
    data = await state.get_data()
    data['language'][int(data_id)][2] = '1' if data_status == '0' else '0'

    await state.update_data(data)
    kb = search.kb_search_checkbox(data['language'], 'language', data["current_page"])
    await call.message.edit_reply_markup(reply_markup=kb)
    await call.answer()

async def page_language(entity: Union[types.Message, types.CallbackQuery], callback_data: dict, state: FSMContext):
    page = callback_data['page']
    data = await state.get_data()

    await state.update_data(current_page=page)
    kb = search.kb_search_checkbox(data['language'], 'language', page)
    await entity.message.edit_reply_markup(reply_markup=kb)
    await entity.answer()


###############
#####TOPIC#####
###############

async def search_topic_list(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    """Display list of all search topic."""
    caption = 'Select topic:'
    data = await state.get_data()
    await state.update_data(current_page="0")

    kb = search.kb_search_checkbox(data['topic'], 'topic')
    if isinstance(entity, types.CallbackQuery):
        await entity.message.edit_text(caption, reply_markup=kb)
        await entity.answer()
        return

    await entity.answer(caption, reply_markup=kb)


async def update_topic(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data_id = callback_data['id']
    data_status = callback_data['status']
    
    data = await state.get_data()
    data['topic'][int(data_id)][2] = '1' if data_status == '0' else '0'

    await state.update_data(data)
    kb = search.kb_search_checkbox(data['topic'], 'topic', data["current_page"])
    await call.message.edit_reply_markup(reply_markup=kb)

async def page_topic(entity: Union[types.Message, types.CallbackQuery], callback_data: dict, state: FSMContext):
    page = callback_data['page']
    data = await state.get_data()

    await state.update_data(current_page=page)
    kb = search.kb_search_checkbox(data['topic'], 'topic', page)
    await entity.message.edit_reply_markup(reply_markup=kb)
    await entity.answer()





################
###SUBSCRIBES###
################

subs_num = {
        "name": ['0', '100', '200', '500', '1000', '2000', '5000', '10000', '20000',
                '50000', '100000', '200000', '500000', '1000000', '2000000', '5000000'],
        "data": ['0', '100', '200', '500', '1000', '2000', '5000', '10000', '20000',
                '50000', '100000', '200000', '500000', '1000000', '2000000', '5000000']
     }

async def search_subs_list(call: types.CallbackQuery, state: FSMContext):
    caption = 'Select <i><b>MIN</b></i> subscribes count:'

    kb = search.kb_search_min_max(subs_num, 'min-subs')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_min_subs(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(min_subs=callback_data["data"])
    caption = 'Select <i><b>MAX</b></i> subcribes count:'
    kb = search.kb_search_min_max(subs_num, 'max-subs')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_max_subs(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(max_subs=callback_data["data"])
    caption = 'Select search filters:'
    kb = search.kb_search()
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


###########
###VIEWS###
###########

views_num = {
        "name": ['10000', '20000', '50000', '100000', '200000', '500000', '1000000', '2000000',
     '5000000', '10000000', '20000000', '50000000', '100000000', '200000000', '500000000', '1000000000'],
        "data": ['10000', '20000', '50000', '100000', '200000', '500000', '1000000', '2000000',
     '5000000', '10000000', '20000000', '50000000', '100000000', '200000000', '500000000', '1000000000']
     }

async def search_views_list(call: types.CallbackQuery, state: FSMContext):
    caption = 'Select <i><b>MIN</b></i> views count:'

    kb = search.kb_search_min_max(views_num, 'min-views')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_min_views(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(min_views=callback_data["data"])
    caption = 'Select <i><b>MAX</b></i> views count:'
    kb = search.kb_search_min_max(views_num, 'max-views')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_max_views(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(max_views=callback_data["data"])
    caption = 'Select search filters:'
    kb = search.kb_search()
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


############
###VIDEOS###
############

videos_num = {
        "name": ['0', '10', '20', '30', '40', '50', '75', '100', '150', '200', '300', '500'],
        "data": ['0', '10', '20', '30', '40', '50', '75', '100', '150', '200', '300', '500']
     }

async def search_videos_list(call: types.CallbackQuery, state: FSMContext):
    caption = 'Select <i><b>MIN</b></i> videos count:'

    kb = search.kb_search_min_max(videos_num, 'min-videos')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_min_videos(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(min_videos=callback_data["data"])
    caption = 'Select <i><b>MAX</b></i> videos count:'
    kb = search.kb_search_min_max(videos_num, 'max-videos')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_max_videos(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(max_videos=callback_data["data"])
    caption = 'Select search filters:'
    kb = search.kb_search()
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()



###############
###############
###############

ago_num = {
    "name": ['1 week', '2 weeks', '1 month', '2 months', '3 months', '6 months', '1 year', '2 years'],
    "data": ['7', '14', '30', '60', '90', '180', '365', '730']
}

############
###LATEST###
############


async def search_latest_list(call: types.CallbackQuery, state: FSMContext):
    caption = 'Select <b>MIN</b> latest video date:'

    kb = search.kb_search_min_max(ago_num, 'min-latest')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_min_latest(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(min_latest=callback_data["data"])
    caption = 'Select <b>MAX</b> latest video date:'
    kb = search.kb_search_min_max(ago_num, 'max-latest')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_max_latest(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(max_latest=callback_data["data"])
    caption = 'Select search filters:'
    kb = search.kb_search()
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


##############
###CREATION###
##############

async def search_creation_list(call: types.CallbackQuery, state: FSMContext):
    caption = 'Select <b>MIN</b> creation date:'

    kb = search.kb_search_min_max(ago_num, 'min-creation')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_min_creation(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(min_creation=callback_data["data"])
    caption = 'Select <b>MAX</b> creation date:'
    kb = search.kb_search_min_max(ago_num, 'max-creation')
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()


async def select_max_creation(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(max_creation=callback_data["data"])
    caption = 'Select search filters:'
    kb = search.kb_search()
    await call.message.edit_text(caption, reply_markup=kb)
    await call.answer()




async def start_search(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    data = await state.get_data()
    category = ', '.join([x[1] for x in data["category"] if x[2] == "1"])
    topic = ', '.join([x[1] for x in data["topic"] if x[2] == "1"])
    language = ', '.join([x[1] for x in data["language"] if x[2] == "1"])
    country = ', '.join([x[1] for x in data["country"] if x[2] == "1"])

    output = (
        '<i>Is that correct?</i>\n\n'
        f'<b>Channel name:</b> <i>{data["name"]}</i> \n' 
        f'<b>Keywords:</b> <i>{data["keyword"]}</i> \n'
        f'<b>Subscribers:</b> <i>MIN({data["min_subs"] if data["min_subs"] != "" else ""}):MAX({data["max_subs"] if data["max_subs"] != "" else ""})</i> \n'
        f'<b>Views:</b> <i>MIN({data["min_views"] if data["min_views"] != "" else ""}):MAX({data["max_views"] if data["max_views"] != "" else ""})</i> \n'
        f'<b>Latest date:</b> <i>MIN({data["min_latest"] if data["min_latest"] != "" else ""} days):MAX({data["max_latest"] if data["max_latest"] != "" else ""} days)</i> \n'
        f'<b>Creation date:</b> <i>MIN({data["min_creation"] if data["min_creation"] != "" else ""} days):MAX({data["max_creation"] if data["max_creation"] != "" else ""} days)</i> \n'
        f'<b>Total video:</b> <i>MIN({data["min_videos"] if data["min_videos"] != "" else ""}):MAX({data["max_videos"] if data["max_videos"] != "" else ""})</i> \n'
        f'<b>Category:</b> <i>{category}</i>\n'
        f'<b>Topics:</b> <i>{topic}</i>\n'
        f'<b>Languages:</b> <i>{language}</i>\n'
        f'<b>Countries:</b> <i>{country}</i>\n'
    )
    
    await entity.message.edit_text(output, reply_markup=search.kb_search_yesno())
    await entity.answer()

async def do_search(entity: Union[types.Message, types.CallbackQuery], state: FSMContext):
    data = await state.get_data()

    youtube = YouTube()
    youtube.set_channel_name(data["name"])
    youtube.set_channel_keywords(data["keyword"])
    youtube.set_channel_subs_min(data["min_subs"])
    youtube.set_channel_subs_max(data["max_subs"])
    youtube.set_channel_views_min(data["min_views"])
    youtube.set_channel_views_max(data["max_views"])
    youtube.set_channel_creation_min(data["min_creation"])
    youtube.set_channel_creation_max(data["max_creation"])
    youtube.set_channel_latest_min(data["min_latest"])
    youtube.set_channel_latest_max(data["max_latest"])
    youtube.set_channel_videos_min(data["min_videos"])
    youtube.set_channel_videos_max(data["max_videos"])

    [youtube.add_category(x[3]) for x in data["category"] if x[2] == "1"]
    [youtube.add_country(x[3]) for x in data["country"] if x[2] == "1"]
    [youtube.add_language(x[3]) for x in data["language"] if x[2] == "1"]
    [youtube.add_topic(x[3]) for x in data["topic"] if x[2] == "1"]

    await entity.message.edit_text("<i>Please wait, the request will take some time...</i>")

    user_id = entity.message.from_user.id
    filename = f"youtube_{user_id}_{strftime('%Y_%m_%d_%H_%M_%S', gmtime())}"
    print(filename)
    youtube.set_csv_filename(filename)
    await youtube.get_channels_info()

    path = youtube.csv_file

    await entity.message.answer_document(open(path, "rb"))