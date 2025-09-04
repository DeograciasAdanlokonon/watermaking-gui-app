import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from watermark import Watermark


class App(ctk.CTk):
    """cutomtkinter GUI interface"""
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.title("Watermarking Desktop")
        self.image_path = ""
        self.watermark = Watermark()

        # appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Select file button
        self.select_button = ctk.CTkButton(
            self,
            text='Choose File', 
            command=self.select_file
            )
        self.select_button.grid(row=0, column=0, padx=40, pady=30)

        # Selected file label
        self.selected_file_label = ctk.CTkLabel(
            self,
            text="No file chosen",
            text_color="white"
        )
        self.selected_file_label.grid(row=0, column=1, padx=0, pady=30, columnspan=1)

        # Watermark text entry
        self.signature_entry = ctk.CTkEntry(
            self,
            width=150,
            height=36,
            placeholder_text="Your watermark text ici..."
        )
        self.signature_entry.grid(row=1, column=0)

        # watermaking process button
        self.watermarking_button = ctk.CTkButton(
            self,
            text="Set Watermark",
            height=36,
            command=self.call_watermarking
        )
        self.watermarking_button.grid(row=1, column=1)

        # message display label
        self.message_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 12)
        )
        self.message_label.grid(row=2, column=1)

        # disable signature_entry and watermaking button
        if self.image_path == "":
            self.signature_entry.configure(state="disabled")
            self.watermarking_button.configure(state="disabled")
        else:
            self.signature_entry.configure(state="normal")
            self.watermarking_button.configure(state="normal")

      
    def call_watermarking(self):
        """
        Calls watermarking engine
        """
        if self.image_path and self.signature_entry != "":
            self.watermark.run_watermarking(
                signature_text=self.signature_entry.get(),
                image_path=self.image_path
            )
        
        # Message label state
        if self.watermark.watermarking_done:
            self.watermarking_button.configure(
                text="Download Output",
                fg_color="green",
                command=self.save_output_file
            )

            self.message_label.configure(
                text = self.watermark.message,
                text_color="green"
            )
        else:
            self.message_label.configure(
                text = self.watermark.message,
                text_color="red"
            )

    def select_file(self):
        """opens file dialogue to select a file"""
        self.image_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(
            ("Image files", "*.jpg"), 
            ("Image files", "*.png"),
            ("Image files", "*.gif") 
            )
        )

        if self.image_path:
            self.selected_file_label.configure(text=f"{self.image_path}")
            self.signature_entry.configure(state="normal")
            self.watermarking_button.configure(state="normal")

    def save_output_file(self):
        """
        Opens a 'Save As' dialog for the user to select a location and filename
        to save the specified output file
        """
        source_file_path = "signed_image.jpg"

        #open the image first
        image_to_save = self.watermark.image

        # Open a "Save As" dialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("GIF files", "*.gif")]
        )

        if file_path:
            try:
                image_to_save.save(file_path)
                tk.messagebox.showinfo("Success", f"Image saved successfully to: {file_path}")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to save image: {e}")
        
    





