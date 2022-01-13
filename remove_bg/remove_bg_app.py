import requests, os, tkinter as tk

class MainApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Remove Background")
        self.master.geometry("500x300")
        self.path_rmvbg = tk.StringVar()
        self.path_downloaded = tk.StringVar()
        self.txt_path_rmv = tk.Entry(self.frame,width=50,justify='center',textvariable=self.path_rmvbg)
        self.txt_path_rmv.insert(0,'masukan path gambar')
        self.txt_path_rmv.pack()
        self.txt_path_ready = tk.Entry(self.frame,width=50,justify='center',textvariable=self.path_downloaded)
        self.txt_path_ready.insert(0,'masukan path downloaded')
        self.txt_path_ready.pack()
        self.button1 = tk.Button(self.frame, text = 'Masukan Path', width = 25, command=self.download_image)
        self.button1.pack()
        self.frame.pack()

    def download_image(self):
        self.text_output = tk.Text(self.master, width=50, height=10)
        self.text_output.pack()
        for filename in os.listdir(self.path_rmvbg.get()):
            f = os.path.join(self.path_rmvbg.get(), filename)

            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(f, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': 'api_key'},
            )
            if response.status_code == requests.codes.ok:
                file_ready = str(self.path_downloaded.get()) + '\\' + filename
                with open(file_ready, 'wb') as out:
                    out.write(response.content)
                self.text_output.insert(tk.END,f"{filename} berhasil di download\n")
            else:
                self.text_output.insert("Error:", response.status_code, response.text)

def main(): 
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
