import sys

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        # Declare widgets
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather!", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):

        # Set Title and Icon
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("3845731.png"))

        # Layout Manager
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Set Alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Set Object Name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Set Style Sheet
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 150px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        print("***************")
        print("Weather fetched!")

        api_key = "03b89f10aa92cf83d16977ca1a788e19"

        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
                print("Success!")

        except requests.exceptions.HTTPError:
            match response.status_code:
                # 1xx Informational
                case 100:
                    self.display_error("ERROR 100\nContinue")
                case 101:
                    self.display_error("ERROR 101\nSwitching Protocols")

                # 2xx Success (other than 200)
                case 201:
                    self.display_error("ERROR 201\nCreated")
                case 202:
                    self.display_error("ERROR 202\nAccepted")
                case 204:
                    self.display_error("ERROR 204\nNo Content")

                # 3xx Redirection
                case 301:
                    self.display_error("ERROR 301\nMoved Permanently")
                case 302:
                    self.display_error("ERROR 302\nFound (Moved Temporarily)")
                case 304:
                    self.display_error("ERROR 304\nNot Modified")
                case 307:
                    self.display_error("ERROR 307\nTemporary Redirect")
                case 308:
                    self.display_error("ERROR 308\nPermanent Redirect")

                # 4xx Client Errors
                case 400:
                    self.display_error("ERROR 400\nBad Request\nPlease check your input")
                case 401:
                    self.display_error("ERROR 401\nUnauthorized\nAuthentication is required")
                case 403:
                    self.display_error("ERROR 403\nForbidden\nYou do not have access")
                case 404:
                    self.display_error("ERROR 404\nResource not found")
                case 405:
                    self.display_error("ERROR 405\nMethod Not Allowed")
                case 406:
                    self.display_error("ERROR 406\nNot Acceptable")
                case 408:
                    self.display_error("ERROR 408\nRequest Timeout")
                case 409:
                    self.display_error("ERROR 409\nConflict")
                case 410:
                    self.display_error("ERROR 410\nGone")
                case 413:
                    self.display_error("ERROR 413\nPayload Too Large")
                case 414:
                    self.display_error("ERROR 414\nURI Too Long\nYour request URL is too long")
                case 415:
                    self.display_error("ERROR 415\nUnsupported Media Type")
                case 418:
                    self.display_error("ERROR 418\nI'm a Teapot\nServer refuses to brew coffee")
                case 421:
                    self.display_error("ERROR 421\nMisdirected Request\nRequest sent to wrong server")
                case 422:
                    self.display_error("ERROR 422\nUnprocessable Entity")
                case 423:
                    self.display_error("ERROR 423\nLocked\nThe resource is locked")
                case 425:
                    self.display_error("ERROR 425\nToo Early\nServer unwilling to process early request")
                case 426:
                    self.display_error("ERROR 426\nUpgrade Required\nClient must switch protocols")
                case 428:
                    self.display_error("ERROR 428\nPrecondition Required\nRequest must be conditional")
                case 429:
                    self.display_error("ERROR 429\nToo Many Requests\nPlease slow down")
                case 431:
                    self.display_error("ERROR 431\nRequest Header Fields Too Large")
                case 451:
                    self.display_error("ERROR 451\nUnavailable For Legal Reasons")

                # 5xx Server Errors
                case 500:
                    self.display_error("ERROR 500\nInternal Server Error")
                case 501:
                    self.display_error("ERROR 501\nNot Implemented")
                case 502:
                    self.display_error("ERROR 502\nBad Gateway")
                case 503:
                    self.display_error("ERROR 503\nService Unavailable")
                case 504:
                    self.display_error("ERROR 504\nGateway Timeout")
                case 505:
                    self.display_error("ERROR 505\nHTTP Version Not Supported")
                case 506:
                    self.display_error("ERROR 506\nVariant Also Negotiates")
                case 507:
                    self.display_error("ERROR 507\nInsufficient Storage")
                case 508:
                    self.display_error("ERROR 508\nLoop Detected")
                case 511:
                    self.display_error("ERROR 511\nNetwork Authentication Required")

                case _:
                    self.display_error(f"Received unexpected status code: {response.status_code}")

        except requests.ConnectionError:
            self.display_error("Connection Error:\nCheck your connection")

        except requests.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")

        except requests.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

        except Exception as e:
            self.display_error(f"An error occurred: {e}")

    def display_error(self, message):
        print(message)
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):

        # Load, Display Temperature
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_f = (temperature_k * 9/5) - 459.67
        temperature_c = temperature_k - 273.15  # Fixed: was 237.15

        print(data["name"])
        print(f"{temperature_k:.0f}°K")
        print(f"{temperature_f:.0f}°F")
        print(f"{temperature_c:.0f}°C")

        self.temperature_label.setText(f"{temperature_c:.0f}°C")

        # Load, Display Weather
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        print(weather_description)
        print(weather_id)

        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)  # Fixed: was temperature_label

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:  # Fixed: was =
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:  # Fixed: was =
            return "🌪️"
        elif weather_id == 800:  # Fixed: was =
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())
