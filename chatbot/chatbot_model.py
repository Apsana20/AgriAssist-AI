def get_answer(question):

    question = question.lower()

    if "crop" in question:
        return "Rice and Wheat are commonly recommended crops."

    elif "fertilizer" in question:
        return "Use fertilizers based on soil nutrients."

    elif "yield" in question:
        return "Adequate rainfall and balanced nutrients improve yield."

    elif "disease" in question:
        return "Monitor crops regularly and apply suitable pesticides."

    else:
        return "Please provide more details."