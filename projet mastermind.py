from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Ellipse
from kivy.uix.spinner import Spinner
from random import randrange
from kivy.core.window import Window
import json
class Mastermind(App):
    def build(self):
        self.title='Mastermind'
        self.box1=BoxLayout(orientation='vertical',spacing=50,padding=50)
        self.nom=''
        self.score=0
        self.answer=[]
        self.liste_choix=[0,0,0,0]
        self.posandcoul=0
        self.onlycoul=0
        self.tentatif=10
        self.cadre1(1)
        self.dicocouleur={'red':[1,0,0],'orange':[1,0.65,0],'yellow':[1,1,0],'green':[0,1,0],'pink':[1,0.41,0.71],'blue':[0,0,1],'grey':[0.66,0.66,0.66],'brown':[0.59,0.29,0]}
        self.texto=''
        self.data=[]
        return self.box1

    def cadre1(self,source):
        self.box1.clear_widgets()
        self.box1line1=BoxLayout(orientation='horizontal')
        self.box1line1.add_widget(Label(text='entrez votre nom: ',size_hint=(0.3,0.3)))
        self.input1=TextInput(multiline=False,size_hint=(1,0.25),text=self.nom)
        self.box1line1.add_widget(self.input1)
        self.box1.add_widget(self.box1line1)

        self.box1line2=BoxLayout(orientation='horizontal')
        self.output = Label(color=[1,0,0,1])
        self.box1line2.add_widget(self.output)
        box1button1=Button(text='ok',size_hint=(0.2,0.2))
        box1button1.bind(on_press=self.buttonok)
        self.box1line2.add_widget(box1button1)
        self.box1.add_widget(self.box1line2)
        return

    def buttonok(self,source):
        self.nom=self.input1.text
        if self.nom.replace(" ","")=='':
            self.output.text='Bien essayé!'

        try:
            with open('Mastermind JSON.txt') as file:
                jeu=json.loads(file.read())
                self.data=jeu
                for elem in jeu:
                    if self.nom in elem:
                        self.score=elem[self.nom]["meilleur score "]
        except:
            pass
        self.cadre2(source)
        return

    def cadre2(self,source):
        self.box1.clear_widgets()
        box2button1=Button(text='Commencer le jeu')
        box2button1.bind(on_press=self.cadre3)
        box2button2=Button(text='Explication du jeu')
        box2button2.bind(on_press=self.explication)
        box2button3=Button(text='Contact')
        box2button3.bind(on_press=self.contact)
        box2button4=Button(text='A propos du jeu')
        box2button4.bind(on_press=self.apropos)
        box2button5=Button(text='Retour')
        box2button5.bind(on_press=self.cadre1)
        self.box1.add_widget(box2button1)
        self.box1.add_widget(box2button2)
        self.box1.add_widget(box2button3)
        self.box1.add_widget(box2button4)
        self.box1.add_widget(box2button5)
        return

    def explication(self,source):
        self.box1.clear_widgets()
        self.box1.add_widget(Label(text='Le jeu "Mastermind" consiste à deviner une combinaison de couleur choisit par le programme\n'\
                                    "\nLe programme vous fournira également des indices et restera afficher tout au long du jeu\n"\
                                    "\nPour le niveau simple, les combinaisons sont composées de 4 couleurs choisit parmi 6.\n"\
                                    "\npour le niveau hard, les combinaisons sont composées de 5 couleurs choisit parmi 8.\n"\
                                    '\nPour avoir la bonne réponse, non seulement la couleur des pions est importante mais aussi leur position.\n'\
                                    "\nLa même couleur peut apparaître plusieurs fois dans la combinaison.\n"\
                                    "\nLe joueur a 10 (ou 12) tentatives pour trouver la bonne combinaison. S'il n'y parvient pas, il perd.\n"\
                                    "\nChaque fois que le joueur confirme sa combianison, il perd une tetative même si la combinaison est bonne\n"\
                                    "\nLorsque que le joueur propose une combinaison, le programme donnera comme indices: \n"\
                                    "\n          1.le nombre de pions à la bonne couleur et en même temps se trouve à la bonne place. \n"\
                                    "\n          2.le nombre de pions à la bonne couleur mais qui se trouvent à la mauvaise place.\n"))
        bou=Button(text='Retour',size_hint=(0.1,0.1),pos_hint={'x':.4, 'y':0})
        bou.bind(on_press=self.cadre2)
        self.box1.add_widget(bou)
        return

    def contact(self,source):
        self.box1.clear_widgets()
        self.box1.add_widget(Label(text="Si vous avez un soucis quelconque, veuillez contacter le responsable du programme:\n\n "\
                                        "Zhao Yiming\n\n 195187@ecam.be"))
        bou=Button(text='Retour',size_hint=(0.1,0.1),pos_hint={'x':.4, 'y':0})
        bou.bind(on_press=self.cadre2)
        self.box1.add_widget(bou)
        return

    def apropos(self,source):
        self.box1.clear_widgets()
        self.box1.add_widget(Label(text="les références consulté sont les suivantes:\n\n"
                                        "http://tableauxmaths.fr/spip/spip.php?article146 \n\n"
                                        "https://quentin.lurkin.xyz/courses/python2ba/projet2020/ \n\n"
                                        "https://docs.python.org/3/library/random.html \n\n"
                                        "https://kivy.org/doc/stable/ \n\n"
                                        "https://kivy.org/doc/stable/api-kivy.uix.spinner.html"))
        bou=Button(text='Retour',size_hint=(0.1,0.1),pos_hint={'x':.4, 'y':0})
        bou.bind(on_press=self.cadre2)
        self.box1.add_widget(bou)
        return
    
    def cadre3(self,source):
        self.box1.clear_widgets()
        self.box1.canvas.clear()
        box3button1=Button(text='Niveau normal')
        box3button1.bind(on_press=self.niveaunormal)
        box3button2=Button(text='Niveau hard')
        box3button2.bind(on_press=self.niveauhard)
        box3button3=Button(text='Retour')
        box3button3.bind(on_press=self.cadre2)
        self.box1.add_widget(box3button1)
        self.box1.add_widget(box3button2)
        self.box1.add_widget(box3button3)
        return

    def niveaunormal(self,source):
        self.texto=''
        self.box1.clear_widgets()
        self.liste_choix=[0,0,0,0]
        self.tentatif=10
        listecoul=['red','orange','yellow','green','pink','blue']
        self.answer=[listecoul[randrange(6)],listecoul[randrange(6)],listecoul[randrange(6)],listecoul[randrange(6)]]
        box4line1=BoxLayout(orientation='horizontal')
        box4button1=Button(text="j'abandonne",size_hint=(0.05,0.5),pos_hint={'x':0, 'y':0.8})
        box4button1.bind(on_press=self.cadre3)
        box4line1.add_widget(box4button1)
        box4line1.add_widget(Label(text='player: '+str(self.nom),size_hint=(0.1,0.1),pos_hint={'x':0, 'y':1}))
        box4line1.add_widget(Label(text='votre meilleur score: '+str(self.score)+' tentative restante',size_hint=(0.1,0.1),pos_hint={'x':0, 'y':1}))
        self.box1.add_widget(box4line1)

        with self.box1.canvas:
            self.cercle1=Ellipse(pos=(50,350), size=(100,100))
            self.cercle2=Ellipse(pos=(250,350), size=(100,100))
            self.cercle3=Ellipse(pos=(450,350), size=(100,100))
            self.cercle4=Ellipse(pos=(650,350), size=(100,100))

        box4line2=BoxLayout(orientation='horizontal',spacing=110)
        self.choix1 = Spinner(text='couleur 1',values=('red','orange','yellow','green','pink','blue'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix1)
        self.choix1.bind(text=self.change_spinner1)

        self.choix2 = Spinner(text='couleur 2',values=('red','orange','yellow','green','pink','blue'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix2)
        self.choix2.bind(text=self.change_spinner2)

        self.choix3 = Spinner(text='couleur 3',values=('red','orange','yellow','green','pink','blue'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix3)
        self.choix3.bind(text=self.change_spinner3)

        self.choix4 = Spinner(text='couleur 4',values=('red','orange','yellow','green','pink','blue'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix4)
        self.choix4.bind(text=self.change_spinner4)
        self.box1.add_widget(box4line2)

        box4line3=BoxLayout(orientation='horizontal')
        self.rest=Label(text='tentatives restantes: '+str(self.tentatif),size_hint=(0.4,0.9),pos_hint={'x':0, 'y':0.2})
        box4line3.add_widget(self.rest)
        box4button2=Button(text='je confirme!!!',size_hint=(0.5,0.3),pos_hint={'x':1 , 'y':0.5})
        box4button2.bind(on_press=self.confirme)
        box4line3.add_widget(box4button2)
        self.box1.add_widget(box4line3)

        box4line4=BoxLayout(orientation='horizontal')
        self.output=Label(size_hint=(1,0),pos_hint={'x':1, 'y':0})
        box4line4.add_widget(self.output)
        self.box1.add_widget(box4line4)
        return
    def change_spinner1(self,spinner,text):
        self.liste_choix[0]=text
        with self.box1.canvas:
            Color(float(self.dicocouleur[text][0]),float(self.dicocouleur[text][1]),float(self.dicocouleur[text][2]))
            self.cercle1=Ellipse(pos=self.cercle1.pos)
        return
    def change_spinner2(self,spinner,text):
        self.liste_choix[1]=text
        with self.box1.canvas:
            Color(float(self.dicocouleur[text][0]),float(self.dicocouleur[text][1]),float(self.dicocouleur[text][2]))
            self.cercle2=Ellipse(pos=self.cercle2.pos)
        return
    def change_spinner3(self,spinner,text):
        self.liste_choix[2]=text
        with self.box1.canvas:
            Color(float(self.dicocouleur[text][0]),float(self.dicocouleur[text][1]),float(self.dicocouleur[text][2]))
            self.cercle3=Ellipse(pos=self.cercle3.pos)
        return
    def change_spinner4(self,spinner,text):
        self.liste_choix[3]=text
        with self.box1.canvas:
            Color(float(self.dicocouleur[text][0]),float(self.dicocouleur[text][1]),float(self.dicocouleur[text][2]))
            self.cercle4=Ellipse(pos=self.cercle4.pos)
        return
    def change_spinner5(self,spinner,text):
        self.liste_choix[4]=text
        with self.box1.canvas:
            Color(float(self.dicocouleur[text][0]),float(self.dicocouleur[text][1]),float(self.dicocouleur[text][2]))
            self.cercle5=Ellipse(pos=self.cercle5.pos)
        return
    def confirme(self,soure):
        try:
            self.tentatif-=1
            self.rest.text='tentatives restantes: '+str(self.tentatif)
            i=0
            while i < len(self.liste_choix):
                if self.answer[i]==self.liste_choix[i]:
                    self.posandcoul+=1
                i+=1
            seq1,seq2=[],[]
            seq1=self.answer.copy()
            seq2=self.liste_choix.copy()
            for item1 in seq1:
                if item1 in seq2:
                    seq2.remove(item1)
                    self.onlycoul+=1
            self.texto+=str(", ".join(self.liste_choix))+" : {} pion(s) de la bonne couleur et bonne place, {} pion(s) de la bonne couleur\n".format(self.posandcoul,self.onlycoul-self.posandcoul)
            self.posandcoul,self.onlycoul=0,0
            self.output.text=self.texto
            if self.answer==self.liste_choix:
                return self.win()
            if self.tentatif==0:
                return self.loss()
            return
        except:
            self.tentatif+=1
            self.posandcoul,self.onlycoul=0,0
            self.rest.text='veuillez choisir toutes les couleurs'
    def win(self):
        self.box1.clear_widgets()
        self.box1.canvas.clear()
        self.box1.add_widget(Label(text='Bien joué '+ self.nom+'! vous avez réussi la partie avec '+str(self.tentatif)+' tentative(s) restantes\n\n'
                                        " (la partie a été automatiquement sauvegardé dans le fichier: 'Mastermind JSON.txt')"))
        box4button1=Button(text='Nouvelle partie')
        box4button1.bind(on_press=self.cadre3)
        self.box1.add_widget(box4button1)
        box4button2=Button(text='Retour au menu')
        box4button2.bind(on_press=self.cadre2)
        self.box1.add_widget(box4button2)
        if self.tentatif>self.score:
            self.score=self.tentatif
        self.data.append({self.nom:{'combianison random ':", ".join(self.answer),'vos combinaisons ':self.texto.split('\n'),
                            "resultat ":"victoire",'score obtenu ':self.tentatif,'meilleur score ':self.score}})
        with open('Mastermind JSON.txt','w',encoding='ascii') as file:
            file.write(json.dumps(self.data,indent=4))
        return

    def loss(self):
        self.box1.clear_widgets()
        self.box1.canvas.clear()
        self.box1.add_widget(Label(text='Dommage, vous avez perdu la partie! \n\n la bonne combinaison des couleurs était: '+", ".join(self.answer)+"\n\n"
                                    " (la partie a été automatiquement sauvegardé dans le fichier: 'Mastermind JSON.txt')"))
        box6button1=Button(text='Recommencer une partie')
        box6button1.bind(on_press=self.cadre3)
        self.box1.add_widget(box6button1)
        box6button2=Button(text='Retour au menu')
        box6button2.bind(on_press=self.cadre2)
        self.box1.add_widget(box6button2)
        self.data.append({self.nom: {'combinaison random ':", ".join(self.answer),'vos combinaisons ':self.texto.split('\n'),'resultat ':"perdu",
                            'score obtenu ':self.tentatif,'meilleur score ':self.score}})
        with open('Mastermind JSON.txt','w',encoding='ascii') as file:
            file.write(json.dumps(self.data,indent=4))
        return

    def niveauhard(self,source):
        self.texto=''
        self.box1.clear_widgets()
        self.liste_choix=[0,0,0,0,0]
        self.tentatif=12
        listecoul=['red','orange','yellow','green','pink','blue','grey','brown']
        self.answer=[listecoul[randrange(8)],listecoul[randrange(8)],listecoul[randrange(8)],listecoul[randrange(8)],listecoul[randrange(8)]]
        box4line1=BoxLayout(orientation='horizontal')
        box4button1=Button(text="j'abandonne",size_hint=(0.05,0.5),pos_hint={'x':0, 'y':0.8})
        box4button1.bind(on_press=self.cadre3)
        box4line1.add_widget(box4button1)
        box4line1.add_widget(Label(text='player: '+str(self.nom),size_hint=(0.1,0.1),pos_hint={'x':0, 'y':1}))
        box4line1.add_widget(Label(text='votre meilleur score: '+str(self.score)+' tentatives restante',size_hint=(0.1,0.1),pos_hint={'x':0, 'y':1}))
        self.box1.add_widget(box4line1)

        with self.box1.canvas:
            self.cercle1=Ellipse(pos=(50,350), size=(100,100))
            self.cercle2=Ellipse(pos=(200,350), size=(100,100))
            self.cercle3=Ellipse(pos=(350,350), size=(100,100))
            self.cercle4=Ellipse(pos=(500,350), size=(100,100))
            self.cercle5=Ellipse(pos=(650,350), size=(100,100))

        box4line2=BoxLayout(orientation='horizontal',spacing=50)
        self.choix1 = Spinner(text='couleur 1',values=('red','orange','yellow','green','pink','blue','grey','brown'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix1)
        self.choix1.bind(text=self.change_spinner1)

        self.choix2 = Spinner(text='couleur 2',values=('red','orange','yellow','green','pink','blue','grey','brown'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix2)
        self.choix2.bind(text=self.change_spinner2)

        self.choix3 = Spinner(text='couleur 3',values=('red','orange','yellow','green','pink','blue','grey','brown'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix3)
        self.choix3.bind(text=self.change_spinner3)

        self.choix4 = Spinner(text='couleur 4',values=('red','orange','yellow','green','pink','blue','grey','brown'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix4)
        self.choix4.bind(text=self.change_spinner4)

        self.choix5 = Spinner(text='couleur 5',values=('red','orange','yellow','green','pink','blue','grey','brown'),size_hint=(0.5,0.3),pos_hint={'x':0, 'y':-0.3},sync_height=50)
        box4line2.add_widget(self.choix5)
        self.choix5.bind(text=self.change_spinner5)
        self.box1.add_widget(box4line2)

        box4line3=BoxLayout(orientation='horizontal')
        self.rest=Label(text='tentative restantes: 12',size_hint=(0.4,0.9),pos_hint={'x':0, 'y':0.2})
        box4line3.add_widget(self.rest)
        box4button2=Button(text='je confirme!!!',size_hint=(0.5,0.3),pos_hint={'x':1 , 'y':0.5})
        box4button2.bind(on_press=self.confirme)
        box4line3.add_widget(box4button2)
        self.box1.add_widget(box4line3)

        box7line4=BoxLayout(orientation='horizontal')
        self.output=Label(size_hint=(1,0),pos_hint={'x':1, 'y':0})
        box7line4.add_widget(self.output)
        self.box1.add_widget(box7line4)
        return


Window.size = (800, 600)
Mastermind().run()
