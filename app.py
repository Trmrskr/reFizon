#!/usr/bin/python3
from models.exam import Exam
from models.user import User
import models


if __name__ == "__main__":
    user = User(first_name="Simon",
		surname="Alale",
		email="simonalale@gmail.com",
		phone_number="08037014954",
		password="82ma72ku76"
	    )

    user.save()

    exam = 
