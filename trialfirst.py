import streamlit as st
from PIL import Image
import base64
import time
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt
import json
import plotly.graph_objects as go
import folium
from folium.plugins import MarkerCluster



st.set_page_config(layout="wide")
# Функция для преобразования изображения в Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def show_sidebar():
    st.sidebar.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        <h1>Beeline Business</h1>
    </div>""", unsafe_allow_html=True)
    
    st.sidebar.markdown(f"""
    <div class="sticker_aftorizations">
        <img src="data:image/png;base64,{sticker_5}" alt="Logo">
    </div>""", unsafe_allow_html=True)
    
    # Добавляем кнопку с обновленным стилем, которая изменяет состояние страницы
    if st.sidebar.button("Авторизация"):
        st.session_state.page = 'second_page' 

# Загрузка изображения логотипа и преобразование его в Base64
image_path = 'pngwingcom.png'  # Путь к вашему изображению
image_path1 = 'pict.png'
sticker = '1.png'
sticker_2 = '2.png'
sticker_3 = '3.png'
sticker_4 = '4.png'
sticker_5 = '5.png'
sticker_7 = '7.png'
sticker_8 = '8.png'
sticker_9 = '9.png'
sticker_10 = '10.png'
logo_base64 = image_to_base64(image_path)
logo_base644 = image_to_base64(image_path1)
sticker = image_to_base64(sticker)
sticker_2 = image_to_base64(sticker_2)
sticker_3 = image_to_base64(sticker_3)
sticker_4 = image_to_base64(sticker_4)
sticker_5 = image_to_base64(sticker_5)
sticker_7 = image_to_base64(sticker_7)
sticker_8 = image_to_base64(sticker_8)
sticker_9 = image_to_base64(sticker_9)
sticker_10 = image_to_base64(sticker_10)

def main_page():
# Стилизация через markdown с HTML и CSS
    st.markdown("""
        <style>      
        /* Стиль верхнего логотипа и заголовка */
        .header {
            background-color: rgb(24,24,24,0.5);
            padding: 20px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            margin-left: -25px;
            z-index: -1;
        }
        .header img {
            margin-left: 0;
            margin-right: 17px;
            max-width: 70px; /* Устанавливаем максимальную ширину для логотипа */
        }
        .header h1 {
            color: yellow;
            font-size: 30px;
            margin: 0;
        }
        .titul {
            color:yellow;
            margin-top: 2%;
            margin-left: 0;
            font-size: 20px;
                    
                }        

        /* Основной блок контента */
    .main-content {
        background-color: #fce106;
        padding: 40px;
        margin: 20px auto; /* Отступ для фиксированного заголовка и боковые отступы */
        border-radius: 30px;
        width: 100%; /* Используем 80% ширины экрана */
        max-width: 1200px; /* Устанавливаем максимальную ширину */
        display: flex;
        align-items: center; /* Вертикальное выравнивание элементов */
        height: 400px;
    }

    .main-content img {
        max-width: 450px; /* Устанавливаем максимальную ширину для изображения */
        margin-right: 20px; /* Отступ между изображением и текстом */
        margin-left: -50px;
    }

    .main-content .text-content {
        display: flex;
        flex-direction: column; /* Вертикальное расположение текста */
        justify-content: center; /* Выравнивание текста по центру вертикально */
    }

    .main-content h2 {
        color: #221e1f;
        font-size: 36px;
        margin-bottom: 30px;
    }

    .main-content p {
        color: #221e1f;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .btn-learn-more {
        background-color: #221e1f;
        color: #000;
        padding: 15px 30px;
        border-radius: 20px;
        font-size: 18px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block; /* Это важно для ограничения ширины */
        width: auto; /* Ширина кнопки будет определяться содержимым */
        max-width: 200px; /* Можно задать максимальную ширину для контроля */
        text-align: center; /* Выравнивание текста внутри кнопки */
    }

    .btn-learn-more:hover {
        background-color: #221e1f;
        color: #fce106;
    }
    .scrolling-wrapper {
            display: flex;
            overflow: hidden;
            width: 100%;
            position: relative;
            padding: 20px;
            background-color: rgb(14, 17, 23); /* Фоновый цвет для контейнера */
        }

        .scrolling-inner {
            display: flex;
            width: 100%;
            animation: scroll 20s linear infinite;
        }

        .card {
            background: linear-gradient(153deg, rgba(0,0,0,1) 0%, rgba(1,1,24,1) 61%, rgba(3,3,43,1) 100%);
            color: white;
            flex: 0 0 auto;
            width: 300px;
            height: 400px;
            margin-right: 70px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        .card h3 {
            color: white;
            font-size: 24px;
        }

        @keyframes scroll {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-100%);
            }
        }
        .card img {
            max-width: 360px; /* Устанавливаем максимальную ширину для изображения */
            margin-right: 0; /* Отступ между изображением и текстом */
            margin-top: -15px;
            margin-left: -60px;
            z-index: 2;
            }       

    .special {
            margin-top: 40px;
            margin-bottom: 20px;
                }
                
    .sticker_aftorizations {
            margin-top: 50%;
            margin-bottom: 20%;
            margin-left: 32%;
            max-width: 100px;
                }       

    .btn-auth {
            background-color: rgb(14, 17, 23); /* Цвет фона кнопки */
            color: yellow; /* Цвет текста кнопки */
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 18px; /* Размер шрифта кнопки */
            text-decoration: none;
            font-weight: bold;
            text-align: center;
            display: block; /* Кнопка будет на всю ширину */
            margin-top: 40px; /* Отступ сверху */
            /*border: 1px solid yellow;*/
        }
        .btn-auth:hover {
            background-color: #ffcc00; /* Цвет фона при наведении */
            color: #000; /* Цвет текста при наведении */
        }       
    section[data-testid="stSidebar"] {
                background-color: rgb(0, 0, 0); /* Задайте нужный цвет фона */
                border-right: 2px solid yellow;
                position: relative;
            }

        </style>
    """, unsafe_allow_html=True)

    show_sidebar()


    st.markdown("""
        <div class="titul">
            <h2>Получи персональное решение для бизнеса</h2>
        </div>
    """, unsafe_allow_html=True)

    # Основное содержимое страницы
    st.markdown(f"""
        <div class="main-content">
            <img src="data:image/png;base64,{logo_base644}" alt="Logo">
            <div class="text-content">
                <h2>Решение на основе Big Data</h2>
                <p>Узнай портрет своей аудитории по своей базе данных. Анализируй поведение, предпочтения и демографические данные, чтобы точнее выстраивать стратегии для продвижения бизнеса!</p>
                <a class="btn-learn-more" href="second_page">Узнать больше</a>
            </div>
        </div>
    """.format(logo_base64=logo_base644), unsafe_allow_html=True)
    # Кнопки категорий
    st.markdown("""
                <div class="text-content">
                <h2 class="special">Ключевые критерии для точного определения целевой аудитории</h2>
                </div>
    """, unsafe_allow_html=True)


    # Генерация карточек с анимацией
    st.markdown(f"""
    <div class="scrolling-wrapper">
        <div class="scrolling-inner">
            <div class="card">
                <h3>Распределение по возрасту.</h3>
                <img src="data:image/png;base64,{sticker}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределения по полу</h3>
                <img src="data:image/png;base64,{sticker_2}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределение по зарплате.</h3>
                <img src="data:image/png;base64,{sticker_3}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределение по интересам.</h3>
                <img src="data:image/png;base64,{sticker_4}" alt="Logo">
            </div>
            <!-- Дублируем карточки для непрерывности анимации -->
            <div class="card">
                <h3>Распределение по возрасту.</h3>
                <img src="data:image/png;base64,{sticker}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределения по полу.</h3>
                <img src="data:image/png;base64,{sticker_2}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределение по зарплате.</h3>
                <img src="data:image/png;base64,{sticker_3}" alt="Logo">
            </div>
            <div class="card">
                <h3>Распределение по интересам.</h3>
                <img src="data:image/png;base64,{sticker_4}" alt="Logo">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



def second_page():
    st.sidebar.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        <h1>Beeline Business</h1>
    </div>""", unsafe_allow_html=True)
    st.markdown("""
        <style>      
        /* Стиль верхнего логотипа и заголовка */
        .header {
            background-color: rgb(24,24,24,0.0);
            padding: 20px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 40%;
            margin-left: -25px;
            z-index: -1;
        }
        .header img {
            margin-top: 0;
            margin-left: 0;
            margin-right: 17px;
            max-width: 70px; /* Устанавливаем максимальную ширину для логотипа */
        }
        .header h1 {
            margin-top: 20%;
            color: yellow;
            font-size: 30px;
            margin: 0;
        }
        section[data-testid="stSidebar"] {
            background-color: rgb(0, 0, 0); /* Задайте нужный цвет фона */
            border-right: 2px solid yellow;
            position: relative;
            }        
}        
                </style>""", unsafe_allow_html=True)
# Функция для отображения страницы авторизации
    st.title("Авторизация")

        # Поля для ввода логина и пароля
    username = st.text_input("Логин")
    password = st.text_input("Пароль", type="password")

        # Кнопка авторизации
    if st.button("Войти", key="enter"):
        if username == "admin" and password == "password":  # Пример проверки
            st.success("Успешный вход!")
            st.session_state.logged_in = True
            st.session_state.page = 'third_page'
        else:
            st.error("Неправильный логин или пароль")

        # Ссылка на восстановление пароля
    st.markdown("[Забыли пароль?](#)")

        # Кнопка для создания новой учетной записи
    if st.button("Создать учетную запись", key="create"):
        st.session_state.page = 'register_page'

    # Функция для отображения страницы создания учетной записи
    def register_page():
        st.title("Создание учетной записи")

        # Поля для регистрации
        new_username = st.text_input("Логин", type="default", key="register_username")
        new_password = st.text_input("Пароль", type="password", key="register_password")
        confirm_password = st.text_input("Повторите пароль", type="password", key="confirm_password")
        company_name = st.text_input("Название организации", type="default", key="name_company")
        company_inn = st.text_input("ИНН организации", type="default", key="inn_company")
        numbers = st.text_input("Контактный номер ответственного сотрудника", type="default", key="number_company")

        # Кнопка для завершения регистрации
        if st.button("Создать учетную запись", key="create_click"):
            if new_password == confirm_password:
                st.success("Учетная запись успешно создана!")
                st.session_state.page = 'login_page'
            else:
                st.error("Пароли не совпадают")

    # Основная функция для управления страницами
    def main_1():
        # Инициализация сессии
        if 'page' not in st.session_state:
            st.session_state.page = 'login_page'
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False

        # Отображение нужной страницы в зависимости от состояния
        if st.session_state.page == 'login_page':
            second_page()
        elif st.session_state.page == 'register_page':
            register_page()

    # Запуск приложения
    main_1()


def third_page():
    st.markdown("""
        <style>      
        /* Стиль верхнего логотипа и заголовка */
        .header {
            background-color: rgb(24,24,24,0.5);
            padding: 20px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            margin-left: -25px;
            z-index: -1;
        }
        .header img {
            margin-left: 0;
            margin-right: 1px;
            max-width: 70px; /* Устанавливаем максимальную ширину для логотипа */
        }
        .header h1 {
            color: yellow;
            font-size: 30px;
            margin: 0;
            margin-top: 1%;
            padding-left: 15px; /* Добавляем пространство между логотипом и заголовком */
            line-height: 1; /* Минимальная высота строки */
            display: inline-block; /* Заголовок не занимает всю ширину */
        }
        section[data-testid="stSidebar"] {
            background-color: rgb(0, 0, 0); /* Задайте нужный цвет фона */
            border-right: 2px solid yellow;
            position: relative;
    }                           
        .pad {
            margin-top:30px;
            margin-bottom:30px;
                }
        .namess {
            margin-top: 10%;
            font-size: 20px;
            color: yellow;
            }        
        .answers {
            margin-bottom: 10%;
            font-size: 20px;    
                }

        .scrolling-wrapper {
            display: flex;
            flex-wrap: wrap;  /* Позволяет переносить карточки на следующую строку */
            justify-content: space-between; /* Равномерное распределение карточек по ширине */
        }
        .scrolling-inner {
            display: flex;
            flex-wrap: wrap;  /* Перенос по строкам */
            gap: 22px;  /* Отступ между карточками */
        }
        .card {
            background: linear-gradient(153deg, rgba(0,0,0,1) 0%, rgba(1,1,24,1) 61%, rgba(3,3,43,1) 100%);
            color: white;
            flex: 0 0 auto;
            width: 230px;
            height: 300px;
            margin-bottom: 20px;  /* Отступ снизу для карточек в разных строках */
            margin-left: 0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            align-items: center; /* Центрирует карточки по вертикали */
        } 
        .card h3 {
            color: white;
            font-size: 20px;
        }
        .card img {
            max-width: 36px; /* Устанавливаем максимальную ширину для изображения */
            margin-right: 0; /* Отступ между изображением и текстом */
            margin-top: -90px;
            margin-left: 90%;
            z-index: 2;
            }  
        .status {
                top-bottom: 30px;
                front-size: 24px;
                }        
        h4 {
                margin-top: -10%;
                }  
        .btn-learn-more {
            background-color: rgb(14, 17, 23); /* Цвет фона кнопки */
            color: yellow; /* Цвет текста кнопки */
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 18px; /* Размер шрифта кнопки */
            text-decoration: none;
            font-weight: bold;
            text-align: center;
            display: block; /* Кнопка будет на всю ширину */
            margin-top: 40px; /* Отступ сверху */
            /*border: 1px solid yellow;*/
        }
        .btn-learn-more:hover {
            background-color: #ffcc00; /* Цвет фона при наведении */
            color: #000; /* Цвет текста при наведении */
        }  

                     
                </style>""", unsafe_allow_html=True)
    
    
    st.sidebar.markdown(f"""
    <div class="header">
        <div class="logo">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo">
            <h1>Beeline Business</h1>
        </div>""", unsafe_allow_html=True)
    
    st.sidebar.markdown(f"""
        <div class="names">
            <div class="pad"></div>                
            <div class="namess">Название Организации:</div>
            <div class=""answers">ООО "ADV Consulting"</div>
            <div class="namess">ИНН Организиции:</div>
            <div class=""answers">000000000</div>
            <div class="namess">Номер Телефона:</div>
            <div class=""answers"> +998 90 000 00 00</div>
            <div class="namess">Статус Организации:</div>
            <div class=""answers">Holding</div>
        </div>    
        <a class="btn-auth" href="#"></a></h2>
        <div class="pad"></div>               
    </div>""", unsafe_allow_html=True)
    
    st.sidebar.button("Изменить статус")
   
    @st.cache_data
    def load_date(path:str):
            data = pd.read_csv(path)
            return data
        

    uploaded_file = st.file_uploader("Загрузите CSV файл", type=["csv"])

    # Статус загрузки файла
    if uploaded_file is not None:
        example_data = {
        'Пол': ['Мужчина', 'Мужчина', 'Мужчина', 'Мужчина', 'Мужчина', 'Женщина', 'Женщина', 'Мужчина', 'Мужчина', 'Женщина', 'Мужчина', 'Женщина', 'Мужчина', 'Женщина'],
        'Возраст': [22, 29, 35, 45, 52, 28, 33, 41, 59, 61, 23, 35, 25, 45],
        'Зарплата': [3000000, 8000000, 6000000, 6000000, 7000000, 8000000, 9000000, 10000000, 11000000, 1200000, 12000000, 7000000, 8000000, 7000000]
    }
        df = pd.DataFrame(example_data)
        st.dataframe(df)
        # Симуляция процесса загрузки
        with st.spinner('Идет загрузка...'):
            time.sleep(3)  # Имитация времени загрузки файла
            st.success("Файл успешно загружен!")
            st.markdown("""
            <style>      
            /* Стиль верхнего логотипа и заголовка */
            .header {
                background-color: rgb(24,24,24,0.5);
                padding: 20px;
                display: flex;
                justify-content: flex-start;
                align-items: center;
                position: fixed;
                width: 100%;
                top: 0;
                margin-left: -25px;
                z-index: -1;
            }
            .header img {
                margin-left: 0;
                margin-right: 1px;
                max-width: 70px; /* Устанавливаем максимальную ширину для логотипа */
            }
            .header h1 {
                color: yellow;
                font-size: 30px;
                margin: 0;
                margin-top: 1%;
                padding-left: 15px; /* Добавляем пространство между логотипом и заголовком */
                line-height: 1; /* Минимальная высота строки */
                display: inline-block; /* Заголовок не занимает всю ширину */
            }
            section[data-testid="stSidebar"] {
                background-color: rgb(0, 0, 0); /* Задайте нужный цвет фона */
                border-right: 2px solid yellow;
                position: relative;
        }                           
            .pad {
                margin-top:30px;
                margin-bottom:30px;
                    }
            .namess {
                margin-top: 10%;
                font-size: 20px;
                color: yellow;
                }        
            .answers {
                margin-bottom: 10%;
                font-size: 20px;    
                    }

            .scrolling-wrapper {
                display: flex;
                flex-wrap: wrap;  /* Позволяет переносить карточки на следующую строку */
                justify-content: space-between; /* Равномерное распределение карточек по ширине */
            }
            .scrolling-inner {
                display: flex;
                flex-wrap: wrap;  /* Перенос по строкам */
                gap: 22px;  /* Отступ между карточками */
            }
            .card {
                background: linear-gradient(153deg, rgba(0,0,0,1) 0%, rgba(1,1,24,1) 61%, rgba(3,3,43,1) 100%);
                color: white;
                flex: 0 0 auto;
                width: 230px;
                height: 300px;
                margin-bottom: 20px;  /* Отступ снизу для карточек в разных строках */
                margin-left: 0;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                align-items: center; /* Центрирует карточки по вертикали */
            } 
            .card h3 {
                color: white;
                font-size: 20px;
            }
            .card img {
                max-width: 36px; /* Устанавливаем максимальную ширину для изображения */
                margin-right: 0; /* Отступ между изображением и текстом */
                margin-top: -90px;
                margin-left: 90%;
                z-index: 2;
                }  
            .status {
                    top-bottom: 30px;
                    front-size: 24px;
                    }        
            h4 {
                    margin-top: -10%;
                    }  
            .btn-learn-more {
                background-color: rgb(14, 17, 23); /* Цвет фона кнопки */
                color: yellow; /* Цвет текста кнопки */
                padding: 10px 20px;
                border-radius: 20px;
                font-size: 18px; /* Размер шрифта кнопки */
                text-decoration: none;
                font-weight: bold;
                text-align: center;
                display: block; /* Кнопка будет на всю ширину */
                margin-top: 40px; /* Отступ сверху */
                /*border: 1px solid yellow;*/
            }
            .btn-learn-more:hover {
                background-color: #ffcc00; /* Цвет фона при наведении */
                color: #000; /* Цвет текста при наведении */
            }  

                        
                    </style>""", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="scrolling-wrapper">
            <h1 class="status">Пакет Статусов</h1>
            <div class="scrolling-inner">
                <div class="card">
                    <h3>Small Business</h3>
                    <img src="data:image/png;base64,{sticker_7}" alt="Logo">
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <h5 class="btn-learn" href="#">Free</h5>
                </div>
                <div class="card">
                    <h3>Medium Business</h3>
                    <img src="data:image/png;base64,{sticker_8}" alt="Logo">
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <a class="btn-learn-more" href="#">Активировать</a>
                </div>
                <div class="card">
                    <h3>Large Business</h3>
                    <img src="data:image/png;base64,{sticker_9}" alt="Logo">
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <a class="btn-learn-more" href="#">Активировать</a>
                </div>
                <div class="card">
                    <h3>Holding</h3>
                    <img src="data:image/png;base64,{sticker_10}" alt="Logo">
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <h4>.</h4>
                    <a class="btn-learn-more" href="#">Активировать</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

         # Page setup
        st.title("Анализ данных")

        selected_package = st.selectbox("Выберите пакет", ["Small Business", "Medium Business", "Large Business", "Holding"])

        data = {
    'Пол': ['Мужчины', 'Женщины', 'Мужчины', 'Мужчины', 'Мужчины', 'Женщины', 'Мужчины', 'Женщины', 'Мужчины', 'Женщины'],
    'Возраст': [22, 34, 45, 29, 31, 50, 40, 27, 35, 29],
    'Зарплата': [7000000, 5000000, 6000000, 4500000, 5500000, 6500000, 7000000, 4800000, 7000000, 6200000]
}
        df = pd.DataFrame(data)

        if st.button("Принять"):
            st.write(f"Пакет выбран: {selected_package}")
            # Show loading spinner
            with st.spinner('Генерация графиков...'):
                time.sleep(2)  # Simulate loading time
                st.success('Графики готовы!')
            if selected_package == "Small Business":    
            # Create a dashboard layout with columns
                col1, col2 = st.columns(2)

                with col1:
                    # Gender distribution pie chart
                    st.subheader("Распределение по полу")
                    gender_counts = df['Пол'].value_counts(normalize=True) * 100  # Calculate percentages
                    fig_gender = px.pie(
                        values=gender_counts.values,
                        names=gender_counts.index,
                        title='Процентное распределение по полу',
                        color_discrete_sequence=['yellow', '#F5F5F5'],  # Set colors
                        hole=0.6  # Открыть центр
                    )
            
                    # Add spacing for centering the chart
                    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
                    st.plotly_chart(fig_gender, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with col2:
                    # Age distribution line chart
                    st.subheader("Распределение по возрасту")
                    age_groups = pd.cut(df['Возраст'], bins=[18, 25, 35, 45, 55, 65, 75], right=False)
                    age_distribution = age_groups.value_counts(normalize=True).sort_index() * 100
                    
                    # Formatting x-axis labels
                    age_labels = [f"{interval.left}-{interval.right}" for interval in age_distribution.index]
                    
                    fig_age = px.line(x=age_labels, y=age_distribution.values, title="Процентное распределение по возрастным группам")
                    fig_age.update_traces(line=dict(color='yellow'))  # Set line color
                    fig_age.update_layout(xaxis_title="Возрастные группы", yaxis_title="Процент")
                    st.plotly_chart(fig_age)

                
                st.subheader("Распределение по возрасту и полу")

                # Создание возрастных групп
                age_bins = [18, 25, 35, 45, 55, 65, 75]
                df['Возраст группа'] = pd.cut(df['Возраст'], bins=age_bins, right=False)
                
                # Расчет процентов по полу в возрастных группах
                age_gender_distribution = df.groupby(['Возраст группа', 'Пол']).size().unstack(fill_value=0)
                age_gender_distribution = age_gender_distribution.div(age_gender_distribution.sum(axis=1), axis=0) * 100
                age_gender_distribution = age_gender_distribution.reset_index()
                
                # Форматирование возрастных групп
                age_gender_distribution['Возраст группа'] = age_gender_distribution['Возраст группа'].astype(str)

                # Создание графика с возрастными группами в центре
                fig_age_gender = go.Figure()

                # Добавление данных для мужчин (слева)
                fig_age_gender.add_trace(go.Bar(
                    y=age_gender_distribution['Возраст группа'],
                    x=-age_gender_distribution['Мужчины'],  # Отрицательные значения для отображения слева
                    name='Мужчины',
                    marker_color='yellow',
                    width=0.4,
                    orientation='h',  # Горизонтальная ориентация
                    texttemplate="%{x:.1f}%",
                    textposition="inside",
                    offset=-0.4
                ))

                # Добавление данных для женщин (справа)
                fig_age_gender.add_trace(go.Bar(
                    y=age_gender_distribution['Возраст группа'],
                    x=age_gender_distribution['Женщины'],  # Положительные значения для отображения справа
                    name='Женщины',
                    marker_color='#F5F5F5',
                    width=0.4,
                    orientation='h',  # Горизонтальная ориентация
                    texttemplate="%{x:.1f}%",
                    textposition="inside",
                    offset=0.4
                ))

                fig_age_gender.update_layout(
                    title="Процентное распределение по возрастным группам и полу",
                    yaxis_title="Возрастные группы",
                    xaxis_title="Процент",
                    yaxis=dict(tickvals=age_gender_distribution['Возраст группа'], ticktext=age_gender_distribution['Возраст группа']),
                    xaxis=dict(range=[-100, 100], title="Процент"),
                    barmode='overlay'
                )

                st.plotly_chart(fig_age_gender)
                
                st.subheader("Географическое расположение")


                # Создание карты с помощью Folium
                m = folium.Map(location=[41.3082, 69.2598], zoom_start=10)

                # Добавление маркеров и больших желтых кругов на карту
                data = {
                    "latitude": [41.299221075113806],
                    "longitude": [69.27337190739082],
                    "names": ["Beruniy"]
                }

                marker_cluster = MarkerCluster().add_to(m)

                for i, row in enumerate(data["latitude"]):
                    folium.Marker(
                        location=[data["latitude"][i], data["longitude"][i]],
                        popup=f"<b>Название:</b> {data['names'][i]}<br><b>Latitude:</b> {data['latitude'][i]}<br><b>Longitude:</b> {data['longitude'][i]}",
                        icon=folium.Icon(color="red", icon="info-sign"),
                    ).add_to(marker_cluster)

                    folium.Circle(
                        location=[data["latitude"][i], data["longitude"][i]],
                        radius=5000,  # Увеличим радиус для желтых кругов
                        color="yellow",
                        fill=True,
                        fill_color="yellow",
                        fill_opacity=0.3,
                    ).add_to(m)

                # Добавляем легенду к карте
                folium.LayerControl().add_to(m)

                

                # Отображение выбранных точек на карт

                map_height = 400  # Уменьшим высоту карты, чтобы она лучше поместилась на странице
                map_width = 900  # Уменьшим ширину карты
                map_html = f'<div style="display: flex; justify-content: center; align-items: center; height: {map_height}px; width: {map_width}px;">' + m.get_root().render() + '</div>'
                st.components.v1.html(map_html, width=map_width, height=map_height)

                #st.markdown("<p style ='color:red;',> Big Data\ Taxonomy <p/>", unsafe_allow_html=True)    

#####################################################################
            elif selected_package == "Medium Business":
                col1, col2 = st.columns(2)

                with col1:
                    # Gender distribution pie chart
                    st.subheader("Распределение по полу")
                    gender_counts = df['Пол'].value_counts(normalize=True) * 100  # Calculate percentages
                    fig_gender = px.pie(
                        values=gender_counts.values,
                        names=gender_counts.index,
                        title='Процентное распределение по полу',
                        color_discrete_sequence=['yellow', '#F5F5F5'],  # Set colors
                        hole=0.6  # Открыть центр
                    )
            
                    # Add spacing for centering the chart
                    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
                    st.plotly_chart(fig_gender, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with col2:
                    # Age distribution line chart
                    st.subheader("Распределение по возрасту")
                    age_groups = pd.cut(df['Возраст'], bins=[18, 25, 35, 45, 55, 65, 75], right=False)
                    age_distribution = age_groups.value_counts(normalize=True).sort_index() * 100
                    
                    # Formatting x-axis labels
                    age_labels = [f"{interval.left}-{interval.right}" for interval in age_distribution.index]
                    
                    fig_age = px.line(x=age_labels, y=age_distribution.values, title="Процентное распределение по возрастным группам")
                    fig_age.update_traces(line=dict(color='yellow'))  # Set line color
                    fig_age.update_layout(xaxis_title="Возрастные группы", yaxis_title="Процент")
                    st.plotly_chart(fig_age)
                col3, col4 = st.columns(2)
            
                with col3:
                    st.subheader("Распределение по возрасту и полу")

                    # Создание возрастных групп
                    age_bins = [18, 25, 35, 45, 55, 65, 75]
                    df['Возраст группа'] = pd.cut(df['Возраст'], bins=age_bins, right=False)
                    
                    # Расчет процентов по полу в возрастных группах
                    age_gender_distribution = df.groupby(['Возраст группа', 'Пол']).size().unstack(fill_value=0)
                    age_gender_distribution = age_gender_distribution.div(age_gender_distribution.sum(axis=1), axis=0) * 100
                    age_gender_distribution = age_gender_distribution.reset_index()
                    
                    # Форматирование возрастных групп
                    age_gender_distribution['Возраст группа'] = age_gender_distribution['Возраст группа'].astype(str)

                    # Создание графика с возрастными группами в центре
                    fig_age_gender = go.Figure()

                    # Добавление данных для мужчин (слева)
                    fig_age_gender.add_trace(go.Bar(
                        y=age_gender_distribution['Возраст группа'],
                        x=-age_gender_distribution['Мужчины'],  # Отрицательные значения для отображения слева
                        name='Мужчины',
                        marker_color='yellow',
                        width=0.4,
                        orientation='h',  # Горизонтальная ориентация
                        texttemplate="%{x:.1f}%",
                        textposition="inside",
                        offset=-0.4
                    ))

                    # Добавление данных для женщин (справа)
                    fig_age_gender.add_trace(go.Bar(
                        y=age_gender_distribution['Возраст группа'],
                        x=age_gender_distribution['Женщины'],  # Положительные значения для отображения справа
                        name='Женщины',
                        marker_color='#F5F5F5',
                        width=0.4,
                        orientation='h',  # Горизонтальная ориентация
                        texttemplate="%{x:.1f}%",
                        textposition="inside",
                        offset=0.4
                    ))

                    fig_age_gender.update_layout(
                        title="Процентное распределение по возрастным группам и полу",
                        yaxis_title="Возрастные группы",
                        xaxis_title="Процент",
                        yaxis=dict(tickvals=age_gender_distribution['Возраст группа'], ticktext=age_gender_distribution['Возраст группа']),
                        xaxis=dict(range=[-100, 100], title="Процент"),
                        barmode='overlay'
                    )

                    st.plotly_chart(fig_age_gender)

                with col4:
                    st.subheader("Распределение по зарплате")

                    # Гистограмма распределения по зарплате
                    salary_distribution = pd.cut(df['Зарплата'], bins=10).value_counts(normalize=True) * 100
                    salary_bins = pd.cut(df['Зарплата'], bins=10).cat.categories

                    # Форматирование меток на оси X
                    salary_labels = [f"{int(interval.left)}-{int(interval.right)}" for interval in salary_bins]

                    fig_salary = px.bar(
                        x=salary_labels, 
                        y=salary_distribution.values,
                        title="Процентное распределение по зарплате"
                    )

                    # Обновление стиля графика
                    fig_salary.update_traces(
                        marker=dict(color='yellow', line=dict(color='black', width=1)),  # Цвет баров и обводка
                        opacity=0.8  # Прозрачность
                    )
                    fig_salary.update_layout(
                        xaxis_title="Группы зарплат",
                        yaxis_title="Процент",
                        xaxis_tickangle=-45,  # Угол наклона меток для лучшего отображения
                    )

                    st.plotly_chart(fig_salary)

                # Пример данных для демонстрации
                    # Пример данных для демонстрации
                    # Пример данных
                        

                    # Заголовок для основной части приложения
                st.subheader("Географическое расположение")


                # Создание карты с помощью Folium
                m = folium.Map(location=[41.3082, 69.2598], zoom_start=10)

                # Добавление маркеров и больших желтых кругов на карту
                data = {
                    "latitude": [41.299221075113806],
                    "longitude": [69.27337190739082],
                    "names": ["Beruniy"]
                }

                marker_cluster = MarkerCluster().add_to(m)

                for i, row in enumerate(data["latitude"]):
                    folium.Marker(
                        location=[data["latitude"][i], data["longitude"][i]],
                        popup=f"<b>Название:</b> {data['names'][i]}<br><b>Latitude:</b> {data['latitude'][i]}<br><b>Longitude:</b> {data['longitude'][i]}",
                        icon=folium.Icon(color="red", icon="info-sign"),
                    ).add_to(marker_cluster)

                    folium.Circle(
                        location=[data["latitude"][i], data["longitude"][i]],
                        radius=5000,  # Увеличим радиус для желтых кругов
                        color="yellow",
                        fill=True,
                        fill_color="yellow",
                        fill_opacity=0.3,
                    ).add_to(m)

                # Добавляем легенду к карте
                folium.LayerControl().add_to(m)

                # Виджет Streamlit для выбора ресторанов DoDo Pizza
                

                map_height = 400  # Уменьшим высоту карты, чтобы она лучше поместилась на странице
                map_width = 900  # Уменьшим ширину карты
                map_html = f'<div style="display: flex; justify-content: center; align-items: center; height: {map_height}px; width: {map_width}px;">' + m.get_root().render() + '</div>'
                st.components.v1.html(map_html, width=map_width, height=map_height)

            #st.markdown("<p style ='color:red;',> Big Data\ Taxonomy <p/>", unsafe_allow_html=True)

            elif selected_package == "Large Business":
                col1, col2 = st.columns(2)

                with col1:
                    # Gender distribution pie chart
                    st.subheader("Распределение по полу")
                    gender_counts = df['Пол'].value_counts(normalize=True) * 100  # Calculate percentages
                    fig_gender = px.pie(
                        values=gender_counts.values,
                        names=gender_counts.index,
                        title='Процентное распределение по полу',
                        color_discrete_sequence=['yellow', '#F5F5F5'],  # Set colors
                        hole=0.6  # Открыть центр
                    )
            
                    # Add spacing for centering the chart
                    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
                    st.plotly_chart(fig_gender, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with col2:
                    # Age distribution line chart
                    st.subheader("Распределение по возрасту")
                    age_groups = pd.cut(df['Возраст'], bins=[18, 25, 35, 45, 55, 65, 75], right=False)
                    age_distribution = age_groups.value_counts(normalize=True).sort_index() * 100
                    
                    # Formatting x-axis labels
                    age_labels = [f"{interval.left}-{interval.right}" for interval in age_distribution.index]
                    
                    fig_age = px.line(x=age_labels, y=age_distribution.values, title="Процентное распределение по возрастным группам")
                    fig_age.update_traces(line=dict(color='yellow'))  # Set line color
                    fig_age.update_layout(xaxis_title="Возрастные группы", yaxis_title="Процент")
                    st.plotly_chart(fig_age)
                col3, col4 = st.columns(2)
            
                with col3:
                    st.subheader("Распределение по возрасту и полу")

                    # Создание возрастных групп
                    age_bins = [18, 25, 35, 45, 55, 65, 75]
                    df['Возраст группа'] = pd.cut(df['Возраст'], bins=age_bins, right=False)
                    
                    # Расчет процентов по полу в возрастных группах
                    age_gender_distribution = df.groupby(['Возраст группа', 'Пол']).size().unstack(fill_value=0)
                    age_gender_distribution = age_gender_distribution.div(age_gender_distribution.sum(axis=1), axis=0) * 100
                    age_gender_distribution = age_gender_distribution.reset_index()
                    
                    # Форматирование возрастных групп
                    age_gender_distribution['Возраст группа'] = age_gender_distribution['Возраст группа'].astype(str)

                    # Создание графика с возрастными группами в центре
                    fig_age_gender = go.Figure()

                    # Добавление данных для мужчин (слева)
                    fig_age_gender.add_trace(go.Bar(
                        y=age_gender_distribution['Возраст группа'],
                        x=-age_gender_distribution['Мужчины'],  # Отрицательные значения для отображения слева
                        name='Мужчины',
                        marker_color='yellow',
                        width=0.4,
                        orientation='h',  # Горизонтальная ориентация
                        texttemplate="%{x:.1f}%",
                        textposition="inside",
                        offset=-0.4
                    ))

                    # Добавление данных для женщин (справа)
                    fig_age_gender.add_trace(go.Bar(
                        y=age_gender_distribution['Возраст группа'],
                        x=age_gender_distribution['Женщины'],  # Положительные значения для отображения справа
                        name='Женщины',
                        marker_color='#F5F5F5',
                        width=0.4,
                        orientation='h',  # Горизонтальная ориентация
                        texttemplate="%{x:.1f}%",
                        textposition="inside",
                        offset=0.4
                    ))

                    fig_age_gender.update_layout(
                        title="Процентное распределение по возрастным группам и полу",
                        yaxis_title="Возрастные группы",
                        xaxis_title="Процент",
                        yaxis=dict(tickvals=age_gender_distribution['Возраст группа'], ticktext=age_gender_distribution['Возраст группа']),
                        xaxis=dict(range=[-100, 100], title="Процент"),
                        barmode='overlay'
                    )

                    st.plotly_chart(fig_age_gender)

                with col4:
                    st.subheader("Распределение по зарплате")

                    # Гистограмма распределения по зарплате
                    salary_distribution = pd.cut(df['Зарплата'], bins=10).value_counts(normalize=True) * 100
                    salary_bins = pd.cut(df['Зарплата'], bins=10).cat.categories

                    # Форматирование меток на оси X
                    salary_labels = [f"{int(interval.left)}-{int(interval.right)}" for interval in salary_bins]

                    fig_salary = px.bar(
                        x=salary_labels, 
                        y=salary_distribution.values,
                        title="Процентное распределение по зарплате"
                    )

                    # Обновление стиля графика
                    fig_salary.update_traces(
                        marker=dict(color='yellow', line=dict(color='black', width=1)),  # Цвет баров и обводка
                        opacity=0.8  # Прозрачность
                    )
                    fig_salary.update_layout(
                        xaxis_title="Группы зарплат",
                        yaxis_title="Процент",
                        xaxis_tickangle=-45,  # Угол наклона меток для лучшего отображения
                    )

                    st.plotly_chart(fig_salary)
                col5, col6 = st.columns(2)
                with col5:
                    st.subheader("Абоненты имеющие автомобили")
                    automobilists_percent = 65
                    fig_speed = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=automobilists_percent,
                        gauge={
                            'axis': {'range': [0, 100], 'visible': False},  # Скрываем шкалу
                            'bar': {'color': "yellow"},  # Цвет указателя
                        },
                        number={'suffix': "%"},  # Добавляем знак процента
                    ))

                    # Убираем фон и делаем график минималистичным
                    fig_speed.update_layout(
                        title_text="Процент абонентов имеющих автомобили",
                        title_font=dict(size=16, color="white"),  # Размер и цвет шрифта заголовка
                        title_x=0,
                        title_xanchor='left',
                        paper_bgcolor="rgba(0,0,0,0)",  # Прозрачный фон
                        plot_bgcolor="rgba(0,0,0,0)",
                        height=400,  # Одинаковая высота
                        margin=dict(l=0, r=0, t=40, b=0)  # Одинаковые отступы
                    )

                    # Отображение графика в Streamlit
                    st.plotly_chart(fig_speed)

                with col6:
                    st.subheader("Тип устройства")

                    # Данные
                    labels = ['iOS', 'Android']
                    values = [33, 67]

                    # Создание круговой диаграммы с отверстием в центре
                    fig_device = go.Figure(data=[go.Pie(
                        labels=labels,
                        values=values,
                        hole=0.6,  # Открытый центр (40%)
                        textinfo='label+percent',  # Отображение меток и процентов
                        textposition='inside',  # Текст внутри сегментов
                        marker=dict(colors=['#F5F5F5', 'yellow'])  # Цвета: iOS (чёрный), Android (жёлтый)
                    )])

                    # Настройка внешнего вида
                    fig_device.update_layout(
                        title_text="Устройства абонентов в процентном соотношении",
                        title_font=dict(size=16, color="white"),
                        title_x=0,
                        paper_bgcolor="rgba(0,0,0,0)",  # Прозрачный фон
                        plot_bgcolor="rgba(0,0,0,0)",
                        height=400,  # Одинаковая высота
                        margin=dict(l=0, r=0, t=40, b=0)  # Одинаковые отступы
                    )

                    # Отображение графика в Streamlit
                    st.plotly_chart(fig_device)

            # Заголовок для основной части приложения
                st.subheader("Географическое расположение абонентов")


                # Создание карты с помощью Folium
                m = folium.Map(location=[41.3082, 69.2598], zoom_start=10)

                # Добавление маркеров и больших желтых кругов на карту
                data = {
                    "latitude": [41.299221075113806],
                    "longitude": [69.27337190739082],
                    "names": ["Beruniy"]
                }

                marker_cluster = MarkerCluster().add_to(m)

                for i, row in enumerate(data["latitude"]):
                    folium.Marker(
                        location=[data["latitude"][i], data["longitude"][i]],
                        popup=f"<b>Название:</b> {data['names'][i]}<br><b>Latitude:</b> {data['latitude'][i]}<br><b>Longitude:</b> {data['longitude'][i]}",
                        icon=folium.Icon(color="red", icon="info-sign"),
                    ).add_to(marker_cluster)

                    folium.Circle(
                        location=[data["latitude"][i], data["longitude"][i]],
                        radius=5000,  # Увеличим радиус для желтых кругов
                        color="yellow",
                        fill=True,
                        fill_color="yellow",
                        fill_opacity=0.3,
                    ).add_to(m)

                # Добавляем легенду к карте
                folium.LayerControl().add_to(m)

                # Виджет Streamlit для выбора ресторанов DoDo Pizza
                

                map_height = 400  # Уменьшим высоту карты, чтобы она лучше поместилась на странице
                map_width = 900  # Уменьшим ширину карты
                map_html = f'<div style="display: flex; justify-content: center; align-items: center; height: {map_height}px; width: {map_width}px;">' + m.get_root().render() + '</div>'
                st.components.v1.html(map_html, width=map_width, height=map_height)

                    #st.markdown("<p style ='color:red;',> Big Data\ Taxonomy <p/>", unsafe_allow_html=True)
                with st.expander("Интересы"):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.button("Недвижимость")
                        st.button("Финансы")
                        st.button("Развлечения")
                    with col2:
                        st.button("Ритейл")
                        st.button("Одежда и обувь")
                        st.button("Спорт")
                    with col3:
                        st.button("Туризм")
                        st.button("Услуги")
                        st.button("Рестораны и кафе")
                    with col4:
                        st.button("Страхование")
                        st.button("Бытовая техника и электроника")
                    st.write("Здесь может быть ваш текст или график.")

                    # Разделение на две колонки
                    st.subheader("Сравнение баз данных")

                    # Создание двух колонок
                    col11, col21 = st.columns([1, 1])

                    with col11:
                        st.subheader("Ваша база")
                        st.markdown("""
                            <style>
                            .name {
                                font-size: 20px;
                                margin-bottom: 20px;
                                margin-right: 20px;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        st.markdown("""
                            <div style="display: flex; flex-wrap: wrap; width: 100%; box-sizing: border-box;">
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div>Недвижимость</div>
                                    <div>Финансы</div>
                                    <div>Развлечения</div>
                                    <div>Ритейл</div>
                                    <div>Одежда и обувь</div>
                                    <div>Спорт</div>
                                    <div>Быт техника</div>
                                    <div>Услуги</div>
                                    <div>Рестораны и кафе</div>
                                    <div>Страхование</div>
                                    <div>Туризм</div>
                                </div>
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div>12%</div>
                                    <div>15%</div>
                                    <div>36%</div>
                                    <div>99%</div>
                                    <div>41%</div>
                                    <div>65%</div>
                                    <div>5%</div>
                                    <div>75%</div>
                                    <div>41%</div>
                                    <div>41%</div>
                                    <div>41%</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                    with col21:
                        st.subheader("Beeline база")
                        st.markdown("""
                            <style>
                            .name {
                                font-size: 20px;
                                margin-bottom: 20px;
                                margin-right: 20px;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        st.markdown("""
                            <div style="display: flex; flex-wrap: wrap; width: 100%; box-sizing: border-box;">
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div style="color: green;">+36%</div>
                                    <div style="color: green;">+23%</div>
                                    <div style="color: green;">+22.23%</div>
                                    <div style="color: #0E1117;">-12%</div>
                                    <div style="color: #0E1117;">-41%</div>
                                    <div style="color: #0E1117;">-65%</div>
                                    <div style="color: green;">+85%</div>
                                    <div style="color: #0E1117;">-75%</div>
                                    <div style="color: green;">+24%</div>
                                    <div style="color: #0E1117;">-16%</div>
                                    <div style="color: #0E1117;">-41%</div>
                                </div>
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: right; font-size: 18px;">
                                    <div>48%</div>
                                    <div>38%</div>
                                    <div>36.1%</div>
                                    <div>87%</div>
                                    <div>0%</div>
                                    <div>0%</div>
                                    <div>90%</div>
                                    <div>0%</div>
                                    <div>65%</div>
                                    <div>25%</div>
                                    <div>0%</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                with st.expander("Собственность"):
                    st.subheader("       ")
                with st.expander("Интернет активность"):   
                    st.subheader("       ")
                with st.expander("Социальные сети"):           
                    st.subheader("       ")      
                with st.expander("Мессенджеры"):           
                    col11, col21 = st.columns([1, 1])

                    with col11:
                        st.subheader("Ваша база")
                        st.markdown("""
                            <style>
                            .name {
                                font-size: 20px;
                                margin-bottom: 20px;
                                margin-right: 20px;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        st.markdown("""
                            <div style="display: flex; flex-wrap: wrap; width: 100%; box-sizing: border-box;">
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div>Telegram</div>
                                    <div>WhatsApp</div>
                                    <div>Viber</div>
                                    <div>Skype</div>
                                </div>
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div>12%</div>
                                    <div>15%</div>
                                    <div>36%</div>
                                    <div>99%</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                    with col21:
                        st.subheader("Beeline база")
                        st.markdown("""
                            <style>
                            .name {
                                font-size: 20px;
                                margin-bottom: 20px;
                                margin-right: 20px;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        st.markdown("""
                            <div style="display: flex; flex-wrap: wrap; width: 100%; box-sizing: border-box;">
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: left; font-size: 18px;">
                                    <div style="color: green;">+36%</div>
                                    <div style="color: green;">+23%</div>
                                    <div style="color: green;">+5%</div>
                                    <div style="color: #0E1117;">-12%</div>
                                </div>
                                <div style="flex: 1; min-width: 100px; box-sizing: border-box; padding: 5px; text-align: right; font-size: 18px;">
                                    <div>48%</div>
                                    <div>38%</div>
                                    <div>41%</div>
                                    <div>87%</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                with st.expander("Премиум сегмент"):           
                    st.subheader("       ")
                with st.expander("Путешествие зарубеж"):           
                    st.subheader("       ")
                with st.expander("Путешествие по Узбекистану"):           
                    st.subheader("       ")                                          
            
            elif selected_package == "Holding":
                st.title("Разрабатываем по индивидуальному заказу")


    else:
        st.info("Пожалуйста, загрузите файл CSV для выбора пакета.")           











def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main_page"
    # Логика переключения страниц
    if st.session_state.page == "main_page":
        main_page()
    elif st.session_state.page == "second_page":
        second_page()
    elif st.session_state.page == "third_page":
        third_page()


main()



