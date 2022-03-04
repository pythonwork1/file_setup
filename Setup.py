from tkinter import *
from git import Repo
import threading
file_name='SetupFile of <#noa>, file={}'.format(__file__)
file_size='600x400'
page1=Tk()
page1.title(file_name)
page1.geometry(file_size)

page1_text=Label(page1, text="©Python-work", font=("Arial",70), fg="green")
page1_text.pack()

def page1_nextp(file_name,file_size):
    page1.destroy()
    page2=Tk()
    page2.title(file_name)
    page2.geometry('700x500')

    page2_text=Label(page2, text="Info:")
    page2_text.pack()

    page2_info=Text(page2)
    page2_info.insert('end','<#mt>\n©Python-work')
    page2_info.pack()

    def page2_nextp(file_name,file_size):
        page2.destroy()
        page3=Tk()
        page3.title(file_name)
        page3.geometry(file_size)

        page3_path=Text(page3, height=1)
        page3_path.insert('end','C:\\Program Files\\')
        page3_path.pack()

        def page3_nextp(file_name,file_size,path):
            page3.destroy()
            def setup(file_name,file_size):
                pageSetup=Tk()
                pageSetup.title(file_name)
                pageSetup.geometry(file_size)

                pageSetup_text1=Label(pageSetup, text="Collecting github link...{}%".format(0))
                pageSetup_text1.pack()

                pageSetup_text2=Label(pageSetup, text="Downloading file...{}%".format(0))
                pageSetup_text2.pack()

                pageSetup_text3=Label(pageSetup, text="Copy new file...{}%".format(0))
                pageSetup_text3.pack()


                def change_pageSetup_collecting(i):
                    pageSetup_text1.config(text="Collecting github link...{}%".format(i))
                for i in range (101):
                    pageSetup.after(10000,lambda:change_pageSetup_collecting(i))
                    
                def change_pageSetup_downloading(i):
                    pageSetup_text2.config(text="Downloading file...{}%".format(i))
                for i in range (101):
                    pageSetup.after(10000,lambda:change_pageSetup_downloading(i))

                def change_pageSetup_copynewfile(i):
                    pageSetup_text3.config(text="Copy new file...{}%".format(i))
                for i in range (101):
                    pageSetup.after(10000,lambda:change_pageSetup_copynewfile(i))

            def download(path):
                Repo.clone_from("<#url>",path)

            download(path)
            setup(file_name,file_size)

        page3_next=Button(page3, text="Next", command=lambda:page3_nextp(file_name,file_size,page3_path.get('1.0','end').strip('\n')))
        page3_next.pack()
        

    page2_next=Button(page2, text="Next",command=lambda:page2_nextp(file_name,file_size))
    page2_next.pack()

page1_next=Button(page1, text="Next", command=lambda:page1_nextp(file_name,file_size))
page1_next.pack()


page1.mainloop()
