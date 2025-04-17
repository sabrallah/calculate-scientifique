import tkinter as tk
import math

class CalculatriceScientifique:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice Scientifique")
        master.configure(bg='#f0f0f0')
        master.resizable(False, False)
        
        # Variables
        self.equation = ""
        self.displayed_equation = ""  # Équation à afficher (plus lisible)
        self.current_input = tk.StringVar()
        self.current_input.set("0")
        self.in_radian_mode = True  # Mode radians par défaut
        
        # Création de l'écran d'affichage
        self.display_frame = tk.Frame(master, bg='#f0f0f0')
        self.display_frame.pack(pady=10)
        
        # Affichage du mode radian/degré
        self.mode_display = tk.Label(self.display_frame, text="RAD", font=('Arial', 10), bg='#f0f0f0')
        self.mode_display.pack(anchor='e', padx=5)
        
        self.display = tk.Entry(self.display_frame, textvariable=self.current_input, font=('Arial', 24), 
                                justify='right', bd=10, insertwidth=4, width=18, bg='#eceff1', readonlybackground='#eceff1')
        self.display.configure(state='readonly')
        self.display.pack()
        
        # Création des boutons
        self.buttons_frame = tk.Frame(master, bg='#f0f0f0')
        self.buttons_frame.pack()
        
        # Bouton de mode RAD/DEG
        self.rad_deg_button = tk.Button(self.buttons_frame, text="RAD/DEG", font=('Arial', 10), 
                                      command=self.toggle_rad_deg, bg='#e1bee7', fg='black', width=8)
        self.rad_deg_button.grid(row=0, column=0, padx=2, pady=2, columnspan=2)
        
        # Définition des boutons - 1ère rangée (fonctions scientifiques)
        scientific_buttons = [
            ('sin', lambda: self.add_trig_function('sin')),
            ('cos', lambda: self.add_trig_function('cos')),
            ('tan', lambda: self.add_trig_function('tan')),
            ('log', lambda: self.add_scientific_function('log10', 'log')),
            ('ln', lambda: self.add_scientific_function('log', 'ln')),
        ]
        
        # Définition des boutons - 2ème rangée (fonctions scientifiques)
        scientific_buttons2 = [
            ('√', lambda: self.add_scientific_function('sqrt', '√')),
            ('x²', lambda: self.add_power_function(2)),
            ('π', lambda: self.add_constant('pi', 'π')),
            ('e', lambda: self.add_constant('e', 'e')),
            ('|x|', lambda: self.add_scientific_function('abs', 'abs')),
        ]
        
        # Définition des boutons - chiffres et opérateurs
        standard_buttons = [
            ('7', lambda: self.add_character('7')), ('8', lambda: self.add_character('8')), ('9', lambda: self.add_character('9')), ('/', lambda: self.add_character('/')), ('C', self.clear),
            ('4', lambda: self.add_character('4')), ('5', lambda: self.add_character('5')), ('6', lambda: self.add_character('6')), ('*', lambda: self.add_character('*')), ('⌫', self.backspace),
            ('1', lambda: self.add_character('1')), ('2', lambda: self.add_character('2')), ('3', lambda: self.add_character('3')), ('-', lambda: self.add_character('-')), ('(', lambda: self.add_character('(')),
            ('0', lambda: self.add_character('0')), ('.', lambda: self.add_character('.')), ('=', self.calculate), ('+', lambda: self.add_character('+')), (')', lambda: self.add_character(')')),
        ]
        
        # Création des boutons de fonctions scientifiques - 1ère rangée
        offset_col = 2  # Décalage pour laisser place au bouton RAD/DEG
        for i, (text, command) in enumerate(scientific_buttons):
            btn = tk.Button(self.buttons_frame, text=text, font=('Arial', 12), width=5, height=2, 
                           command=command, bg='#bbdefb', fg='black')
            btn.grid(row=0, column=i+offset_col, padx=5, pady=2)  # Augmenter padx de 2 à 5
        
        # Création des boutons de fonctions scientifiques - 2ème rangée
        for i, (text, command) in enumerate(scientific_buttons2):
            btn = tk.Button(self.buttons_frame, text=text, font=('Arial', 12), width=5, height=2, 
                           command=command, bg='#bbdefb', fg='black')
            btn.grid(row=1, column=i, padx=5, pady=2)  # Augmenter padx de 2 à 5
        
        # Création des boutons standards
        row_offset = 2  # Commencer après les rangées scientifiques
        for i, (text, command) in enumerate(standard_buttons):
            row, col = divmod(i, 5)
            
            if text in ['C', '⌫']:
                bg_color = '#ffcdd2'  # Rouge clair pour effacer
            elif text == '=':
                bg_color = '#a5d6a7'  # Vert clair pour =
            elif text in ['+', '-', '*', '/', '(', ')']:
                bg_color = '#fff59d'  # Jaune clair pour opérateurs
            else:
                bg_color = '#e0e0e0'  # Gris clair pour chiffres
                
            btn = tk.Button(self.buttons_frame, text=text, font=('Arial', 12), width=5, height=2, 
                           command=command, bg=bg_color, fg='black')
            btn.grid(row=row+row_offset, column=col, padx=5, pady=2)  # Augmenter padx de 2 à 5
        
        # Ajouter raccourcis clavier
        master.bind('<Return>', lambda event: self.calculate())
        master.bind('<BackSpace>', lambda event: self.backspace())
        master.bind('c', lambda event: self.clear())
        
        # Ajouter la gestion complète du clavier
        master.bind('<Key>', self.handle_key_press)
    
    def toggle_rad_deg(self):
        self.in_radian_mode = not self.in_radian_mode
        if self.in_radian_mode:
            self.mode_display.config(text="RAD")
        else:
            self.mode_display.config(text="DEG")
    
    def add_character(self, char):
        if self.current_input.get() == "0" and char not in ['.', '+', '-', '*', '/']:
            self.equation = char
            self.displayed_equation = char
        else:
            self.equation += char
            self.displayed_equation += char
        self.update_display()
    
    def add_scientific_function(self, func_name, display_name):
        # Ajoute une fonction scientifique avec un nom d'affichage convivial
        full_func = f"math.{func_name}("
        self.equation += full_func
        self.displayed_equation += f"{display_name}("
        self.update_display()
    
    def add_trig_function(self, func_name):
        # Ajoute une fonction trigonométrique en tenant compte du mode radians/degrés
        self.equation += f"math.{func_name}("
        
        # Si en mode degrés, ajouter la conversion
        if not self.in_radian_mode:
            self.equation += "math.radians("
            self.displayed_equation += f"{func_name}(°"
        else:
            self.displayed_equation += f"{func_name}("
        
        self.update_display()
    
    def add_constant(self, const_name, display_symbol):
        # Ajoute une constante mathématique
        self.equation += f"math.{const_name}"
        self.displayed_equation += display_symbol
        self.update_display()
    
    def add_power_function(self, power):
        # Spécifiquement pour x²
        self.equation += f"**{power}"
        self.displayed_equation += f"²"
        self.update_display()
    
    def calculate(self):
        try:
            if self.equation:
                # Compter les parenthèses ouvrantes et fermantes
                open_parentheses = self.equation.count('(')
                close_parentheses = self.equation.count(')')
                
                # Si en mode degrés, fermer les parenthèses supplémentaires pour radians()
                temp_equation = self.equation
                if not self.in_radian_mode:
                    # Compter les fonctions trigonométriques en mode degrés
                    trig_funcs_count = (temp_equation.count('math.sin(math.radians(') + 
                                      temp_equation.count('math.cos(math.radians(') + 
                                      temp_equation.count('math.tan(math.radians('))
                    
                    # Ajouter des parenthèses fermantes pour les conversions radians()
                    for _ in range(trig_funcs_count):
                        temp_equation += ')'
                
                # Ajouter les parenthèses manquantes
                if open_parentheses > close_parentheses:
                    temp_equation += ')' * (open_parentheses - close_parentheses)
                
                result = eval(temp_equation)
                
                # Formater le résultat pour éviter des nombres à virgule inutiles
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        # Limiter à 8 décimales max
                        result = round(result, 8)
                
                self.equation = str(result)
                self.displayed_equation = str(result)
                self.update_display()
        except ZeroDivisionError:
            self.equation = ""
            self.displayed_equation = ""
            self.current_input.set("Erreur: Division par zéro")
        except ValueError as e:
            self.equation = ""
            self.displayed_equation = ""
            if "math domain error" in str(e):
                self.current_input.set("Erreur: Domaine mathématique")
            else:
                self.current_input.set(f"Erreur: {str(e)[:20]}")
        except Exception as e:
            self.equation = ""
            self.displayed_equation = ""
            self.current_input.set(f"Erreur: {str(e)[:20]}")
    
    def clear(self):
        self.equation = ""
        self.displayed_equation = ""
        self.current_input.set("0")
    
    def backspace(self):
        # Gestion spéciale pour les fonctions et opérations multi-caractères
        if self.equation.endswith('math.sin(math.radians('):
            self.equation = self.equation[:-22]
            self.displayed_equation = self.displayed_equation[:-5]  # 'sin(°'
        elif self.equation.endswith('math.cos(math.radians('):
            self.equation = self.equation[:-22]
            self.displayed_equation = self.displayed_equation[:-5]  # 'cos(°'
        elif self.equation.endswith('math.tan(math.radians('):
            self.equation = self.equation[:-22]
            self.displayed_equation = self.displayed_equation[:-5]  # 'tan(°'
        elif self.equation.endswith('math.sin('):
            self.equation = self.equation[:-9]
            self.displayed_equation = self.displayed_equation[:-4]  # 'sin('
        elif self.equation.endswith('math.cos('):
            self.equation = self.equation[:-9]
            self.displayed_equation = self.displayed_equation[:-4]  # 'cos('
        elif self.equation.endswith('math.tan('):
            self.equation = self.equation[:-9]
            self.displayed_equation = self.displayed_equation[:-4]  # 'tan('
        elif self.equation.endswith('math.log10('):
            self.equation = self.equation[:-11]
            self.displayed_equation = self.displayed_equation[:-4]  # 'log('
        elif self.equation.endswith('math.log('):
            self.equation = self.equation[:-9]
            self.displayed_equation = self.displayed_equation[:-3]  # 'ln('
        elif self.equation.endswith('math.sqrt('):
            self.equation = self.equation[:-10]
            self.displayed_equation = self.displayed_equation[:-2]  # '√('
        elif self.equation.endswith('math.pi'):
            self.equation = self.equation[:-7]
            self.displayed_equation = self.displayed_equation[:-1]  # 'π'
        elif self.equation.endswith('math.e'):
            self.equation = self.equation[:-6]
            self.displayed_equation = self.displayed_equation[:-1]  # 'e'
        elif self.equation.endswith('math.abs('):
            self.equation = self.equation[:-9]
            self.displayed_equation = self.displayed_equation[:-4]  # 'abs('
        elif self.equation.endswith('**2'):
            self.equation = self.equation[:-3]
            self.displayed_equation = self.displayed_equation[:-1]  # '²'
        elif self.equation.endswith('math.radians('):
            self.equation = self.equation[:-13]
            self.displayed_equation = self.displayed_equation[:-2]  # Supprime le symbole degré
        else:
            self.equation = self.equation[:-1] if self.equation else ""
            self.displayed_equation = self.displayed_equation[:-1] if self.displayed_equation else ""
        
        if not self.equation:
            self.current_input.set("0")
        else:
            self.update_display()
    
    def update_display(self):
        # Affiche l'équation en format lisible
        self.current_input.set(self.displayed_equation)
    
    def handle_key_press(self, event):
        key = event.char
        # Gestion des chiffres et opérateurs basiques
        if key.isdigit() or key in ['+', '-', '*', '/', '.', '(', ')']:
            self.add_character(key)
        # Touche Entrée pour calculer
        elif key == '\r':
            self.calculate()
        # Touche Retour arrière pour effacer
        elif key == '\x08':
            self.backspace()
        # Touche 'c' ou 'C' pour effacer tout
        elif key.lower() == 'c':
            self.clear()
        # Touches pour fonctions scientifiques
        elif key.lower() == 's':  # sin
            self.add_trig_function('sin')
        elif key.lower() == 'o':  # cos
            self.add_trig_function('cos')
        elif key.lower() == 't':  # tan
            self.add_trig_function('tan')
        elif key.lower() == 'l':  # log
            self.add_scientific_function('log10', 'log')
        elif key.lower() == 'n':  # ln (log naturel)
            self.add_scientific_function('log', 'ln')
        elif key.lower() == 'r':  # racine carrée (sqrt)
            self.add_scientific_function('sqrt', '√')
        elif key.lower() == 'p':  # pi
            self.add_constant('pi', 'π')
        elif key.lower() == 'e':  # e (constante d'Euler)
            self.add_constant('e', 'e')
        elif key.lower() == 'a':  # abs (valeur absolue)
            self.add_scientific_function('abs', 'abs')
        elif key == '^' or key == '²':  # puissance 2
            self.add_power_function(2)
        elif key == '=':  # égal pour calculer (alternative à Entrée)
            self.calculate()
        elif key.lower() == 'd':  # toggle entre degrés et radians
            self.toggle_rad_deg()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatriceScientifique(root)
    root.mainloop()