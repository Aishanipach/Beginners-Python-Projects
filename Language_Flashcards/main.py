from Gui import Main_app




if __name__ == "__main__":
    app = Main_app(None)
    app.title('my application')
    app.geometry("500x600")
    app.resizable(False, False)
    app.mainloop()