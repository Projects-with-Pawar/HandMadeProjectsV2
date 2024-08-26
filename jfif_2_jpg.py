from PIL import Image
import os

def convertJfifToJpg(inputFilePath: str, outputFilePath: str) -> None:
    """
    Converts a .jfif file to .jpg format.

    :param inputFilePath: Path to the input .jfif file.
    :param outputFilePath: Path where the output .jpg file will be saved.
    """
    try:
        # Open the .jfif file
        with Image.open(inputFilePath) as img:
            # Convert and save the image as .jpg
            img.convert("RGB").save(outputFilePath, "JPEG")
        print(f"File converted and saved to {outputFilePath}")
    except Exception as e:
        print(f"Error | action: convertJfifToJpg | file: {__file__} | line: {e.__traceback__.tb_lineno} | message: {str(e)}")

# Example usage
inputPath = "static/project_img/hardware/MIT Transform Smart Desk/transform.jfif"
outputPath = "static/project_img/hardware/MIT Transform Smart Desk/transform.jpg"
convertJfifToJpg(inputPath, outputPath)
