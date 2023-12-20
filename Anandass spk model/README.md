# UAS SPK MODEL
# Ananda Yusuf Siswanto
# 201011401145 | 07TPLP013

## Virtualenv

install, create, activate virtual environment using virtualenv

https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Install depedencies

run `pip install -r requirements.txt`

## create postgresql database

create database in your locals

modify settings.py

## create table

run:

    python main.py create_table

## create data dan table


INSERT INTO public.laptop_asus (brand,ram,prosesor,"storage",baterai,harga,webcam) VALUES
	 ('ASUS Vivobook Pro 16X OLED N7601','16 GB','Intel Core i9-12900H','1 TB','90WHrs','Rp.33.999.000','1080P'),
	 ('ASUS Zenbook Pro 14 Duo OLED UX8402','16 GB','Intel Core i7-12700H','512 GB','76WHrs','Rp.29.999.000','720P'),
	 ('ASUS Zenbook 14X OLED Space Edition UX5401','16 GB','Intel Core i7-12700H','1 TB','63WHrs','Rp.26.999.000','720P'),
	 ('ASUS Vivobook Pro 15X OLED K6501','16 GB','Intel Core i7-12650H','512 GB','76WHrs','Rp.24.499.000','1080P'),
	 ('ASUS Zenbook S 13 OLED UM5302','16 GB','AMD Ryzen 7 6800U','1 TB','67WHrs','Rp.19.999.000','720P'),
	 ('ASUS Vivobook 14X OLED A1403','8 GB','Intel Core i5-12500H','512 GB','70WHrs','Rp.14.299.000','720P'),
	 ('ASUS Vivobook S 14 OLED K3402','8 GB','Intel Core i5-12500H','512 GB','70WHrs','Rp.13.799.000','720P'),
	 ('ASUS Zenbook 14 UM425UA','8 GB','AMD Ryzen 5 5500U','512 GB','63WHrs','Rp.12.799.000','720P'),
	 ('ASUS Vivobook Go 14 Flip TP1400','4 GB','Intel Pentium Silver N6000','256 GB','39WHrs','Rp.7.566.000','729P'),
	 ('ASUS Vivobook 15 A1502','4 GB','Intel Core i3-1215U','512 GB','42WHrs','Rp.8.499.000','720P');

## run SAW

     python main.py saw

## run WP

    python main.py wp



