import os
import re
import pyttsx3 as voice
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class VariableFinder(App):
    def build(self):
        self.title = 'SearchingForFiles'
        self.voze = voice.init(driverName='sapi5')
        self.voze.setProperty('rate', 140)

        layout = BoxLayout(orientation='vertical')

        title_label = Label(text=self.title, halign='center', size_hint=(1, None), height=100)
        title_label.color = (0.1, 0.5, 1, 1)
        title_label.font_size = 24
        title_label.bold = True

        self.text_input = TextInput(hint_text='Ingrese la ruta completa del archivo:', height=100)
        self.pattern_input = TextInput(hint_text='Patrón de búsqueda (por ejemplo, $CFG->)')
        self.repeat_input = TextInput(hint_text='Eliminar duplicados (Sí/No)', height=100)
        self.search_button = Button(text='Buscar', on_press=self.search_variables)
        
        layout.add_widget(title_label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.pattern_input)
        layout.add_widget(self.repeat_input)
        layout.add_widget(self.search_button)
        
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout

    def search_variables(self, instance):
        carpeta = fr'{self.text_input.text.strip()}'
        patron = fr'\{self.pattern_input.text.strip()}\w+'
        eliminar_duplicados = self.should_eliminate_duplicates(self.repeat_input.text.strip())

        def buscar_variables(ruta_archivo):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    coincidencias = re.findall(patron, contenido)
                    return coincidencias
            except Exception as e:
                print(f"Error al analizar el archivo {ruta_archivo}: {e}")
                return []

        def analizar_carpeta(carpeta):
            resultados = []
            for directorio_raiz, _, archivos in os.walk(carpeta):
                for archivo in archivos:
                    ruta_archivo = os.path.join(directorio_raiz, archivo)
                    coincidencias = buscar_variables(ruta_archivo)
                    if coincidencias:
                        resultados.append((ruta_archivo, coincidencias))
            return resultados

        resultados = analizar_carpeta(carpeta)

        total_coincidencias = sum(len(coincidencias) for _, coincidencias in resultados)

        variables = set()  # Utilizamos un conjunto para almacenar variables únicas
        for _, coincidencias in resultados:
            variables.update(coincidencias)

        if eliminar_duplicados:
            variables = list(variables)

        df = pd.DataFrame({'Variables': variables})

        df.to_csv('variables.csv', index=False)

        self.result_label.text = f'Resultados guardados en "variables.csv". Total de coincidencias: {total_coincidencias}'
        self.speak("Resultados guardados en variables.csv. Total de coincidencias: " + str(total_coincidencias))
        self.show_popup()

    def should_eliminate_duplicates(self, input_text):
        input_text_lower = input_text.lower()
        return input_text_lower == 'sí' or input_text_lower == 'si'

    def show_popup(self):
        content = BoxLayout(orientation="vertical")
        label = Label(text="¿Desea abrir el archivo CSV?")
        button_yes = Button(text="Sí", on_press=self.open_csv)
        button_no = Button(text="No", on_press=self.close_popup)
        
        content.add_widget(label)
        content.add_widget(button_yes)
        content.add_widget(button_no)
        
        self.popup = Popup(title="Abrir archivo", content=content, size_hint=(None, None), size=(300, 200))
        self.popup.open()

    def open_csv(self, instance):
        archivo_a_abrir = "variables.csv"
        if os.path.exists(archivo_a_abrir):
            os.startfile(archivo_a_abrir)
        self.popup.dismiss()

    def close_popup(self, instance):
        self.popup.dismiss()

    def speak(self, text):
        self.voze.say(text)
        self.voze.runAndWait()

if __name__ == '__main__':
    VariableFinder().run()
