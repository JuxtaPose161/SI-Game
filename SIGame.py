import tkinter as tk
import pyglet
import random
pyglet.font.add_file('FuturaCondensedPlain.ttf')


class ButtonQst(tk.Button):
    def __init__(self, master, x, y,qst_type, *args, **kwargs):
        super(ButtonQst, self).__init__(master,*args,**kwargs)
        self.x = x
        self.y = y
        self.special_qst = None
        self.qst_type = qst_type
class SIGame:

    root = tk.Tk()
    root.title('SI Game 1.1')

    def __init__(self):
        self.main_frm = tk.Frame(SIGame.root)
        #Field_BLOCK
        self.field_frm = tk.Frame(self.main_frm)
        self.buttons_frm = tk.Frame(self.field_frm)
        for i in range(8):
            self.buttons_frm.rowconfigure(i, weight=1)
            for j in range(10):
                self.buttons_frm.columnconfigure(j, weight=1)
        self.themes = ('Пожарная безопасность','Терроризм','ЧС военного характера','Массовые беспорядки',\
                       'Охрана труда','Защита территорий и населения','Аварийно-спасательные работы','Общие вопросы')
        #Question_BLOCK
        self.qst_field = []
        #
        self.main_frm.pack(fill='both', expand=True)

    def place_qst_frame(self, row, column, special_qst, qst_type):
        self.qst_frm = tk.Frame(self.main_frm)
        main_wrapper = tk.Frame(self.qst_frm,
                                bg='blue')
        main_wrapper.pack(side='left',fill='both', expand=True)
        double_wrapper = tk.Frame(main_wrapper)
        double_wrapper.pack(side='left',fill='both', expand=True)
        wrapper1 = tk.Frame(double_wrapper)
        tk.Label(wrapper1,
                 text=self.qst_field[row][column][0],
                 bg='blue',
                 fg='yellow',
                 font=('FuturaCondensedPlain', 28),
                 ).pack(fill='both', expand=True)
        if qst_type == 'где логика?':
            self.img1 = tk.PhotoImage(file=f'img/img{row}{column}1.png')
            self.img2 = tk.PhotoImage(file=f'img/img{row}{column}2.png')
            img_frm = tk.Frame(wrapper1)
            lbl1 = tk.Label(img_frm, image=self.img1, bg='blue')
            lbl2 = tk.Label(img_frm, image=self.img2, bg='blue')
            lbl1.pack(side='left', fill='both', expand=True)
            lbl2.pack(side='left', fill='both', expand=True)
            img_frm.pack(fill='both',expand=True)
        elif qst_type == 'вопрос по фото':
            self.img1 = tk.PhotoImage(file=f'img/img{row}{column}.png')
            img_frm = tk.Frame(wrapper1)
            lbl1 = tk.Label(img_frm, image=self.img1, bg='blue')
            lbl1.pack(side='left', fill='both', expand=True)
            img_frm.pack(fill='both', expand=True)
        wrapper2 = tk.Frame(double_wrapper,
                                 bg='blue',
                                 height=150)
        wrapper3 = tk.Frame(double_wrapper,
                                 bg='blue')
        ent = tk.Entry(wrapper3,
                            width=60)
        ent.pack(side='left', expand=True)

        def click_exit_btn():
            self.qst_frm.destroy()
            self.field_frm.pack(side='left', fill='both', expand=True)
        def get_ans():
            ans = ent.get()
            if special_qst == 'Общий вопрос':
                ans = ans.split(';')
                if qst_type == 'перечислить ответы':
                    l = []
                    for a in ans:
                        a = a.split(',')
                        l.append(a)
                    ans = l
                count = 1
                count_qst = len(self.qst_field[row][column][1])
                ans_list = []
                for a in ans:
                    if qst_type == 'перечислить ответы':
                        count_ans = 0
                        for an in a:
                            if an in self.qst_field[row][column][1]:
                                count_ans+=1
                        percent = int((count_ans/count_qst)*100)
                        ans_list.append((count, f'{percent}% правильности'))
                    else:
                        if a.lower() == self.qst_field[row][column][1][0].lower():
                            ans_list.append(count)
                    count+=1
                text1 = f'''Правильные ответы у команд: 
                    {ans_list}

                Правильный ответ: '''
            elif qst_type == 'перечислить ответы':
                ans = ans.split(',')
                count_qst = len(self.qst_field[row][column][1])
                count_ans = 0
                for a in ans:
                    if a in self.qst_field[row][column][1]:
                        count_ans+=1
                percent = int((count_ans/count_qst)*100)
                text1 = f'''Процент правильности: 
                    {percent}%

                Правильный ответ: '''
            elif self.qst_field[row][column][1][0].lower() == ans.lower():
                text1 = f'''Правильно

                Правильный ответ:'''
            else:
                text1 = f'''Неправильно

                Правильный ответ:'''
            double_wrapper.destroy()
            text2 = ',\n'.join(self.qst_field[row][column][1])
            tk.Label(main_wrapper,
                     text=f'''{text1} {text2}''',
                     bg='blue',
                     fg='yellow',
                     font=('FuturaCondensedPlain', 28),
                     ).pack(fill='both', expand=True)
            try:
                self.img_right = tk.PhotoImage(file=f'img/img{row}{column}rg.png')
                tk.Label(main_wrapper, image=self.img_right, bg='blue').pack(fill='both', expand=True)
            except:
                pass
            tk.Button(main_wrapper,
                      text='Выход',
                      bd=5,
                      bg='blue',
                      fg='yellow',
                      font=('FuturaCondensedPlain', 28),
                      command=click_exit_btn,
                      ).pack(side='bottom', expand=True)
        tk.Button(wrapper3,
                  text='Ввод',
                  bd=5,
                  bg='blue',
                  fg='yellow',
                  font=('FuturaCondensedPlain', 28),
                  command=get_ans,
                  ).pack(side='left')
        tk.Label(wrapper3,
                 bg='blue',
                 width=30).pack(side='left')
        wrapper1.pack(fill='both', expand=True)
        wrapper2.pack(side='bottom', fill='x')
        wrapper3.pack(side='bottom', fill='x')
        self.qst_frm.pack(side='left', fill='both', expand=True)

    def place_special_qst_frm(self, special_qst):
        self.special_qst_frm = tk.Frame(self.main_frm,
                                        bg='blue')
        def btn_command():
            self.special_qst_frm.destroy()
            self.qst_frm.pack(side='left', fill='both', expand=True)

        spcl_lbl = tk.Label(self.special_qst_frm,
                       text=str(special_qst),
                       bg='blue',
                       fg='yellow',
                       font=('FuturaCondensedPlain', 48))
        spcl_btn = tk.Button(self.special_qst_frm,
                text='Далее',
                bg='blue',
                fg='yellow',
                bd=5,
                font=('FuturaCondensedPlain',36),
                command=btn_command)
        spcl_frm = tk.Frame(self.special_qst_frm,
                        bg='blue',
                        height=40)
        spcl_lbl.pack(fill='both', expand=True)
        spcl_btn.pack()
        spcl_frm.pack(side='bottom', fill='x')
        self.special_qst_frm.pack(fill='both', expand=True)
    def place_command(self,x,y):
        self.buttons[x][y]['command']=self.root.destroy
    def click_button(self, x, y, special_qst, qst_type):
        self.buttons[x][y].config(state='disabled', bg='grey')
        self.field_frm.pack_forget()
        self.place_qst_frame(x, y, special_qst, qst_type)
        if special_qst != None:
            self.qst_frm.pack_forget()
            self.place_special_qst_frm(special_qst)

    def create_qst_field(self):
        self.qst_field = []
        for row in range(8):
            row_list = []
            for column in range(10):
                row_list.append([str(row),str(column),None])
            self.qst_field.append(row_list)
        for num in range(8):
            with open(f'questions/qsts{num}.txt', 'r', encoding='utf-8') as file:
                rows = file.readlines()
                count = 0
                for row in rows:
                    row = row.split(';')
                    self.qst_field[num][count][0] = row[0].replace('*','\n')
                    self.qst_field[num][count][1] = row[1].split(',')
                    self.qst_field[num][count][2] = row[2].replace('\n','').lower()
                    count+=1
    def create_buttons(self):
        self.buttons = []
        special_qst_list = [i for i in range(1,81)]
        random.shuffle(special_qst_list)
        btn_number = 1
        for row in range(8):
            row_list = []
            for column in range(10):
                field_button = ButtonQst(self.buttons_frm,
                                        x=row,
                                        y=column,
                                        qst_type=self.qst_field[row][column][2],
                                        text=f'{(column + 1) * 100}',
                                        bd=5,
                                        bg='blue',
                                        fg='yellow',
                                        disabledforeground='lightgreen',
                                        font=('FuturaCondensedPlain', 28),)
                count = 0
                for k in special_qst_list[:15]:
                    if btn_number == k:
                        if count<=4:
                            field_button.special_qst = 'Аукцион'
                        elif count<=7:
                            field_button.special_qst = 'Кот в мешке'
                        elif count<=10:
                            field_button.special_qst = 'Вопрос без риска'
                        elif count<=14:
                            field_button.special_qst = 'Общий вопрос'
                    count+=1
                field_button.config(command=lambda btn=field_button: self.click_button(btn.x, btn.y, btn.special_qst, btn.qst_type))
                btn_number+=1
                row_list.append(field_button)
            self.buttons.append(row_list)

    def place_field_frm(self):
        themes_frm = tk.Frame(self.field_frm)
        for i in range(8):
            themes_frm.rowconfigure(i, weight=1)
            theme_lbl = tk.Label(themes_frm,
                                 text=f'{self.themes[i]}',
                                 relief=tk.GROOVE,
                                 bg='blue',
                                 fg='yellow',
                                 width=32,
                                 font=('FuturaCondensedPlain', 24,)
                                 )
            theme_lbl.grid(row=i, column=0, sticky="nsew")
        themes_frm.pack(side='left', fill='y')
        for buttons_row in self.buttons:
            for btn in buttons_row:
                btn.grid(row=btn.x, column=btn.y, sticky='nsew')
        self.buttons_frm.pack(side='left', fill='both', expand=True)
        self.field_frm.pack(side='left', fill='both', expand=True)

    def start(self):
        SIGame.root.geometry('1920x1080')

        self.create_qst_field()
        self.create_buttons()
        self.place_field_frm()
        SIGame.root.mainloop()

g = SIGame()
g.start()
