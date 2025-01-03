import TKinterModernThemes as TKMT
from tkinter import ttk, Variable, messagebox


class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("Сурудин Андрей 23 ВТ-1", "sun-valley", "dark", True, True)
        self.q_numb = 0
        self.frame = ttk.Frame(name='main')
        self.d_name = ttk.Label(self.frame.master, text='Дисциплина: Программирование')
        self.t_name = ttk.Label(self.frame.master, text='Тема: "Условный оператор в Python"')
        self.start_btn = ttk.Button(self.frame.master, text='Начать тестирование', command=self.start_test)
        self.test = []
        ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10 = Variable(), Variable(), Variable(), Variable(), Variable(), Variable(), Variable(), Variable(), Variable(), Variable()
        self.vars = {
            0: ans1,
            1: ans2,
            2: ans3,
            3: ans4,
            4: ans5,
            5: ans6,
            6: ans7,
            7: ans8,
            8: ans9,
            9: ans10
        }
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.d_name.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.t_name.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.start_btn.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.read_file()
        self.run(cleanresize=False)

    def start_test(self):
        self.generate_widgets()

    def read_file(self):                                                                #
        with open('tests.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()
            ans_index = content.index('Ответы:\n')
            for i in range(len(content)):
                if content[i] == '\n' and content[i + 1] != 'Ответы:\n':
                    ans_index += 1
                    question = {'title': content[i + 1].rstrip(),
                                'answers': [content[i + 2].rstrip(), content[i + 3].rstrip(),
                                            content[i + 4].rstrip(), content[i + 5].rstrip()],
                                'true': content[ans_index].rstrip()}
                    self.test += [question]

    def end_test(self):
        k = 0
        label = ttk.Label(self.frame.master, text='Вы завершили тестирование')
        label3 = ttk.Label(self.frame.master, text='Правильные ответы:')
        answers = []
        for i in self.vars.values():
            answers += [i]
        for i in range(len(self.vars)):
            if self.test[i]['true'] == answers[i].get():                                        #
                color = 'green'
                k += 1
            else:
                color = 'red'
            quest = ttk.Label(self.frame.master,
                              text=f'{i + 1}) {self.test[i]["true"]} (Ваш ответ: "{answers[i].get()}")',
                              background=color)
            quest.grid(row=i + 4, column=0, padx=10, pady=10, sticky='nsew')
        label2 = ttk.Label(self.frame.master, text=f'Вы набрали {k} балл(-а)(-ов) из 10 возможных')
        label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        label2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        label3.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

    def on_click(self):
        result = messagebox.askquestion('Диалоговое окно', 'Вы точно хотите завершить тест?')
        if result == 'yes':
            for i in self.frame.master.winfo_children():
                i.destroy()
            self.end_test()

    def next_test(self):
        self.q_numb += 1
        self.generate_widgets()

    def prev_test(self):
        self.q_numb -= 1
        self.generate_widgets()

    def generate_widgets(self):
        question = ttk.Label(self.frame.master, text=f'Вопрос номер { self.q_numb + 1}')
        title = ttk.Label(self.frame.master, text=self.test[self.q_numb]['title'])
        end_btn = ttk.Button(self.frame.master, text='Завершить тест', command=self.on_click)
        next_btn = ttk.Button(self.frame.master, name='next', text='Следующий вопрос', command=self.next_test)
        prev_btn = ttk.Button(self.frame.master, name='back', text='Предыдущий вопрос', command=self.prev_test)
        answer1 = ttk.Radiobutton(self.frame.master, text=self.test[self.q_numb]['answers'][0],
                                  value=self.test[self.q_numb]['answers'][0], variable=self.vars[self.q_numb])
        answer2 = ttk.Radiobutton(self.frame.master, text=self.test[self.q_numb]['answers'][1],
                                  value=self.test[self.q_numb]['answers'][1], variable=self.vars[self.q_numb])
        answer3 = ttk.Radiobutton(self.frame.master, text=self.test[self.q_numb]['answers'][2],
                                  value=self.test[self.q_numb]['answers'][2], variable=self.vars[self.q_numb])
        answer4 = ttk.Radiobutton(self.frame.master, text=self.test[self.q_numb]['answers'][3],
                                  value=self.test[self.q_numb]['answers'][3], variable=self.vars[self.q_numb])
        if self.q_numb != 0:
            prev_btn.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')
        else:
            prev_btn.destroy()
        if self.q_numb != 9:
            next_btn.grid(row=6, column=2, padx=10, pady=10, sticky='nsew')
        else:
            next_btn.destroy()
            prev_btn.grid(row=6, column=2, padx=10, pady=10, sticky='nsew')
        question.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        end_btn.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        title.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        answer1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        answer2.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
        answer3.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
        answer4.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')


if __name__ == "__main__":
    App()
# как выводится на экран
# где команда для чтения файла
