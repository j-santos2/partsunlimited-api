USE parts_unlimited;
-- parts_unlimited.part definition

CREATE TABLE IF NOT EXISTS `part` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `sku` varchar(30) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `weight_ounces` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
);

-- parts_unlimited.part insert data
INSERT INTO parts_unlimited.part (name,sku,description,weight_ounces,is_active) VALUES
	 ('Heavy coil','SDJDDH8223DHJ','Tightly wound nickel-gravy alloy spring',22,1),
	 ('Reverse lever','DCMM39823DSJD','Attached to provide inverse leverage',9,0),
	 ('Macrochip','OWDD823011DJSD','Used for heavy-load computing',2,1);
