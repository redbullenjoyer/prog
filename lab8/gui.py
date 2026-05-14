
import tkinter as tk
from tkinter import scrolledtext
from scraper import NewsScraper

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Новостной парсер")
        self.root.geometry("650x550")
        
        self.label = tk.Label(root, text="Новостные заголовки", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=22)
        self.text_area.pack(pady=10)
        
        self.button = tk.Button(root, text="Обновить новости", command=self.update_news)
        self.button.pack(pady=10)
        
        self.status = tk.Label(root, text="Нажмите 'Обновить'", fg="gray")
        self.status.pack()
        
        self.scraper = NewsScraper("")
        
        self.update_news()
    
    def update_news(self):
        self.text_area.delete(1.0, tk.END)
        self.status.config(text="Загрузка...", fg="orange")
        self.button.config(state=tk.DISABLED)
        self.root.update()
        
        news_list = self.scraper.get_news()
        
        for i, title in enumerate(news_list, 1):
            self.text_area.insert(tk.END, f"{i}. {title}\n\n")
        
        self.status.config(text=f"Загружено {len(news_list)} новостей", fg="green")
        self.button.config(state=tk.NORMAL)