FROM python
WORKDIR /client_colors
COPY . /client_colors
CMD [ "python3", "client_colors.py" ]

