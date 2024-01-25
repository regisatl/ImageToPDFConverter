import tkinter as tk  # Importe le module tkinter pour créer l'interface utilisateur.
from tkinter import (
    filedialog,
)  # Importe le module filedialog pour ouvrir une boîte de dialogue de sélection de fichiers.
from reportlab.pdfgen import canvas  # Importe le module canvas pour créer un PDF.
from PIL import Image  # Importe le module Image pour ouvrir et manipuler des images.
import os  # Importe le module os pour interagir avec le système d'exploitation.


class ImageToPDFConverter:  # Définit une classe pour convertir des images en PDF.
    def __init__(self, root):  # Initialise l'objet avec la fenêtre racine tkinter.
        self.root = root  # Stocke la fenêtre racine.
        self.image_paths = (
            []
        )  # Crée une liste vide pour stocker les chemins des images sélectionnées.
        self.output_pdf_name = (
            tk.StringVar()
        )  # Crée une variable tkinter pour stocker le nom du PDF de sortie.
        self.selected_images_listbox = tk.Listbox(
            root, selectmode=tk.MULTIPLE
        )  # Crée une liste pour afficher les images sélectionnées.

        self.initialize_ui()  # Appelle la fonction pour initialiser l'interface utilisateur.

    def initialize_ui(self):  # Fonction pour initialiser l'interface utilisateur.
        title_label = tk.Label(
            self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold")
        )  # Crée un label pour le titre.
        title_label.pack(pady=10)  # Affiche le label sur l'interface utilisateur.

        selected_images_button = tk.Button(
            self.root, text="Select Images", command=self.selected_images
        )  # Crée un bouton pour sélectionner des images.
        selected_images_button.pack(
            pady=(0, 10)
        )  # Affiche le bouton sur l'interface utilisateur.

        self.selected_images_listbox.pack(
            pady=(0, 10), fill=tk.BOTH, expand=True
        )  # Affiche la liste des images sélectionnées sur l'interface utilisateur.

        label = tk.Label(
            self.root, text="Enter output PDF name:"
        )  # Crée un label pour le nom du PDF de sortie.
        label.pack()  # Affiche le label sur l'interface utilisateur.

        pdf_name_entry = tk.Entry(
            self.root, textvariable=self.output_pdf_name, width=40, justify="center"
        )  # Crée une entrée pour le nom du PDF de sortie.
        pdf_name_entry.pack()  # Affiche l'entrée sur l'interface utilisateur.

        convert_button = tk.Button(
            self.root, text="Convert to PDF", command=self.convert_image_to_pdf
        )  # Crée un bouton pour convertir les images en PDF.
        convert_button.pack(
            pady=(20, 40)
        )  # Affiche le bouton sur l'interface utilisateur.

    def select_images(self):  # Fonction pour sélectionner des images.
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )  # Ouvre une boîte de dialogue pour sélectionner des images.
        self.update_selected_images_listbox()  # Met à jour la liste des images sélectionnées.

    def update_selected_images_listbox(
        self,
    ):  # Fonction pour mettre à jour la liste des images sélectionnées.
        self.selected_images_listbox.delete(
            0, tk.END
        )  # Efface la liste des images sélectionnées.

        for image_path in self.image_paths:  # Pour chaque chemin d'image sélectionné,
            _, image_path = os.path.split(
                image_path
            )  # obtient le nom du fichier image.
            self.selected_images_listbox.insert(
                tk.END, image_path
            )  # Ajoute le nom du fichier image à la liste des images sélectionnées.

    def convert_image_to_pdf(self):  # Fonction pour convertir les images en PDF.
        if not self.image_paths:  # Si aucune image n'est sélectionnée,
            return  # retourne sans rien faire.

        output_pdf_path = (
            self.output_pdf_name.get() + ".pdf"
            if self.ouptut_pdf_name.get()
            else "output.pdf"
        )  # Obtient le nom du PDF de sortie.

        pdf = canvas.Canvas(
            output_pdf_path, pagesize=(612, 792)
        )  # Crée un nouveau PDF.

        for image_path in self.image_paths:  # Pour chaque image sélectionnée,
            img = Image.open(image_path)  # ouvre l'image.
            available_width = 540  # Définit la largeur disponible pour l'image.
            available_height = 720  # Définit la hauteur disponible pour l'image.
            scale_factor = min(
                available_width / img.width, available_height / img.height
            )  # Calcule le facteur d'échelle pour adapter l'image à la taille disponible.
            new_width = (
                img.width * scale_factor
            )  # Calcule la nouvelle largeur de l'image.
            new_height = (
                img.height * scale_factor
            )  # Calcule la nouvelle hauteur de l'image.
            x_centered = (
                612 - new_width
            ) / 2  # Calcule la position x pour centrer l'image.
            y_centered = (
                792 - new_height
            ) / 2  # Calcule la position y pour centrer l'image.

            pdf.setFillColorRGB(
                255, 255, 255
            )  # Définit la couleur de remplissage en blanc.
            pdf.rect(
                0, 0, 612, 792, fill=True
            )  # Dessine un rectangle blanc pour effacer la page.
            pdf.drawInlineImage(
                img, x_centered, y_centered, width=new_width, height=new_height
            )  # Dessine l'image sur la page.

            pdf.showPage()  # Termine la page actuelle et en commence une nouvelle.

        pdf.save()  # Sauvegarde le PDF.


def main():  # Fonction principale.
    root = tk.Tk()  # Crée une nouvelle fenêtre tkinter.
    root.title("Image to PDF")  # Définit le titre de la fenêtre.
    converter = ImageToPDFConverter(root)  # Crée un nouvel objet ImageToPDFConverter.
    root.geometry("400x600")  # Définit la taille de la fenêtre.
    root.mainloop()  # Démarre la boucle principale de tkinter.


if __name__ == "__main__":  # Si le script est exécuté directement,
    main()  # appelle la fonction principale.
else:  # sinon,
    pass  # ne fait rien.