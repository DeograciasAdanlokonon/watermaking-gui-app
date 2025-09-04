from PIL import Image, ImageDraw, ImageFont

class Watermark:
  """Watermaking object"""
  def __init__(self):
    self.image = None
    self.font = ImageFont.truetype("arial.ttf", 30) # font Arial, size 30
    self.message = ""
    self.watermarking_done = False

  def run_watermarking(self, signature_text, image_path):
    """
    Runs watermarking process

    signature_text(str): the signature text
    image_path(str): an image path
    """
    
    self.add_text_signature(signature_text, image_path)
    self.save_image()

  def save_image(self):
    """saves output image"""

    output_path = "signed_image.jpg"  # name to save the new image on
    self.image.save(output_path)

  def add_text_signature(self, signature_text, image_path):
    """
    Adds text signature on image and returns it

    signature_text(str): the signature text
    image_path(str): an image path
    """
    draw = self.image_draw(image_path)
    text_color = (0, 0, 0)  # black color (R, G, B)
    self.font = ImageFont.truetype("arial.ttf", self.image.width * 0.02) # dynamic font size
    text_position = (20, self.image.height - (self.image.height * 0.08))  # anchor coordinates of the text

    try:

      draw.text(text_position, signature_text, fill=text_color, font=self.font)
      self.watermarking_done = True
      self.message = "Watermarking Successfully Done!"
      print("Signature added!")

    except Exception as e:
      self.message = f"Error: {e}"
      print(f"Error: {e}")   

  def image_draw(self, image_path):
    """
    Draws image and returns it

    image_path(str): an image path
    """
    try:
      self.open_image(image_path=image_path)
      draw = ImageDraw.Draw(self.image)
      
      return draw
    except Exception as e:
      self.message = f"Error: {e}"
      print(f"Error: {e}")
  
  def open_image(self, image_path):
    """
    Opens image

    image_path(str): the image path to be open
    """
    try:
      self.image = Image.open(image_path)
    except FileNotFoundError:
      self.message = "Error: No file found. Try again!"
      print("Unable to open the image")

