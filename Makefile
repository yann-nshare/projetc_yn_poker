##
## EPITECH PROJECT, 2019
## day10 task01
## File description:
## 
##



SRC	=	src/main.py \
		src/Class.py

NAME 	=	poker

all: 	$(NAME)
############create lybrairies ###################
$(NAME):
	chmod +x $(SRC)
	cp src/main.py $(NAME)

############clean files tmp and *.o##############
clean:
	rm -f $(NAME)

############clean *.o and $(NAME)################
fclean:	clean
	find . -name "*[#|~]" -delete  -o -name "[#]*" -delete

re:	clean all

auteur:
	echo $(USER) > auteur
