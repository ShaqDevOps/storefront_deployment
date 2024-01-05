-- SQL queries to insert products
-- SQL queries to insert products without collection_id and last_update
-- SQL queries to insert products with their respective collection_id



-- SQL queries to insert collections
INSERT INTO store_collection (title)
VALUES 
('Litter & Hygiene'),
('Comfort & Bedding'),
('Toys & Entertainment'),
('Grooming'),
('Feeding Essentials'),
('Health & Wellness');



INSERT INTO store_product (title, slug, description, unit_price, inventory, collection_id)
VALUES 
('Anti-splash Litter Box', 'anti-splash-litter-box', '', 15.00, 10, 1),
('DownyPaws Smart Cat Litter Odor Purifier', 'downypaws-smart-cat-litter-odor-purifier', '', 30.00, 10, 1),
('Kattenbak Waterproof Pet Cat Litter Mat', 'kattenbak-waterproof-pet-cat-litter-mat', '', 10.00, 10, 1),
('PETKIT PURA MAX Self Cleaning Litter Box', 'petkit-pura-max-self-cleaning-litter-box', '', 650.00, 10, 1),
('Petland Tofu Cat Litter One box (6 packs) 36L', 'petland-tofu-cat-litter-one-box', '', 70.00, 10, 1),
('Petree APP controlled Self Cleaning Litter Box', 'petree-app-controlled-self-cleaning-litter-box', '', 600.00, 10, 1),
('Comfortable Breathable Cotton Cat Bed', 'comfortable-breathable-cotton-cat-bed', '', 25.00, 10, 2),
('Automatic Rolling Ball Toy', 'automatic-rolling-ball-toy', '', 15.00, 10, 3),
('Feather Toys', 'feather-toys', '', 3.50, 10, 3),
('Interactive Catnip Ball', 'interactive-catnip-ball', '', 5.50, 10, 3),
('Natural Catnip Cat Wall Stick-on', 'natural-catnip-cat-wall-stick-on', '', 3.00, 10, 3),
('Pumpkin Pet Brush', 'pumpkin-pet-brush', '', 12.00, 10, 4),
('Pet Hair Roller Remove', 'pet-hair-roller-remove', '', 3.00, 10, 4),
('Soft Silicone Bath Brush', 'soft-silicone-bath-brush', '', 5.00, 10, 4),
('Stainless Steel Cat Bowl', 'stainless-steel-cat-bowl', '', 10.00, 10, 5),
('Natural Catnip Sticks', 'natural-catnip-sticks', '', 2.00, 10, 6),
('Stainless Steel Cat Bowl', 'stainless-steel-cat-bowl', '', 10.00, 10, 5);