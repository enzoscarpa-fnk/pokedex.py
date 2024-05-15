"""
Pokédex
__author__ = 'FNK'
__version__ = '0.4'
"""

import sqlite3
import ttkbootstrap as tkb
import tkinter as tk
import pygame
import pygame.mixer
import pyglet
from time import sleep
from tkinter import *
from PIL import Image, ImageTk


# POKEMON VALUES FOR DATABASE --------------------

pokedex_data = [('001', 'BULBIZARRE', 'GRAINE', '0.7m', '6.9kg', "Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/001.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/001.wav'),
('002', 'HERBIZARRE', 'GRAINE', '1.0m', '13.0kg', "Son bulbe dorsal devient si gros qu'il ne peut plus se tenir sur ses membres postérieurs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/002.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/002.wav'),
('003', 'FLORIZARRE', 'GRAINE', '2.0m', '100.0kg', "Sa plante mûrit en absorbant les rayons du soleil. Il migre souvent vers les endroits ensoleillés.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/003.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/003.wav'),
('004', 'SALAMECHE', 'LEZARD', '0.6m', '8.5kg', "Il préfère les endroits chauds. En cas de pluie, de la vapeur se forme autour de sa queue.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/004.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/004.wav'),
('005', 'REPTINCEL', 'FLAMME', '1.1m', '19.0kg', "En agitant sa queue, il peut élever le niveau de la température à un degré incroyable.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/005.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/005.wav'),
('006', 'DRACAUFEU', 'FLAMME', '1.7m', '90.5kg', "Il peut fondre la roche de son souffle brûlant. Il est souvent la cause d'énormes incendies.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/006.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/006.wav'),
('007', 'CARAPUCE', 'MINITORTUE', '0.5m', '9.0kg', "Son dos durcit avec l'âge et devient une super carapace. Il peut cracher des jets d'écume.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/007.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/007.wav'),
('008', 'CARABAFFE', 'TORTUE', '1.0m', '22.5kg', "Il se cache au fond de l'eau pour guetter sa proie. Ses oreilles sont des gouvernails.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/008.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/008.wav'),
('009', 'TORTANK', 'CARAPACE', '1.6m', '85.5kg', "Un Pokémon brutal armé de canons hydrauliques. Ses puissants jets d'eau sont dévastateurs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/009.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/009.wav'),
('010', 'CHENIPAN', 'VER', '0.3m', '2.9kg', "Ses petites pattes sont équipées de ventouses, lui permettant de grimper aux murs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/010.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/010.wav'),
('011', 'CHRYSACIER', 'COCON', '0.7m', '9.9kg', "Il est vulnérable aux attaques tant que sa carapace fragile expose son corps tendre et mou.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/011.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/011.wav'),
('012', 'PAPILUSION', 'PAPILLON', '1.1m', '32.0kg', "En combat il bat des ailes très rapidement pour jeter sur ses ennemis des poudres toxiques.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/012.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/012.wav'),
('013', 'ASPICOT', 'INSECTOPIC', '0.3m', '3.2kg', "Il se nourrit de feuilles dans les forêts. L'aiguillon sur son front est empoisonné.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/013.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/013.wav'),
('014', 'COCONFORT', 'COCON', '0.6m', '10.0kg', "Incapable de se déplacer de lui-même, il se défend en durcissant sa carapace.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/014.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/014.wav'),
('015', 'DARDARGNAN', 'GUEPOISON', '1.0m', '29.5kg', "Il vole à très grande vitesse. Il se bat avec les dards empoisonnés de ses bras.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/015.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/015.wav'),
('016', 'ROUCOOL', 'MINOISEAU', '0.3m', '1.8kg', "Il est souvent vu dans les forêts. Il brasse l'air de ses ailes près du sol pour projeter du sable.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/016.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/016.wav'),
('017', 'ROUCOUPS', 'OISEAU', '1.1m', '30.0kg', "Il protège son territoire avec ardeur et repousse à coups de bec tout individu.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/017.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/017.wav'),
('018', 'ROUCARNAGE', 'OISEAU', '1.5m', '39.5kg', "Il chasse en survolant la surface de l'eau et en plongeant pour attraper des proies faciles.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/018.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/018.wav'),
('019', 'RATTATA', 'SOURIS', '0.3m', '3.5kg', "Sa morsure est très puissante. Petit et rapide, on en voit un peu partout.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/019.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/019.wav'),
('020', 'RATTATAC', 'SOURIS', '0.7m', '18.5kg', "Si ses moustaches sont coupées, il perd le sens de son équilibre et devient moins rapide.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/020.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/020.wav'),
('021', 'PIAFABEC', 'MINOISEAU', '0.3m', '2.0kg', "Il chasse les insectes dans les hautes-herbes. Ses petites ailes lui permettent de voler très vite.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/021.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/021.wav'),
('022', 'RAPASDEPIC', 'BEC-OISEAU', '1.2m', '38.0kg', "Ses ailes géantes lui permettent de planer si longtemps qu'il ne se pose que très rarement.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/022.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/022.wav'),
('023', 'ABO', 'SERPENT', '2.0m', '6.9kg', "Il se déplace en silence pour dévorer des oeufs de Roucool ou de Piafabec.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/023.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/023.wav'),
('024', 'ARBOK', 'COBRA', '3.5m', '65.0kg', "Les motifs féroces peints sur son corps changent selon son environnement.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/024.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/024.wav'),
('025', 'PIKACHU', 'SOURIS', '0.4m', '6.0kg', "Quand plusieurs de ces Pokémon se réunissent, ils provoquent de gigantesques orages.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/025.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/025.wav'),
('026', 'RAICHU', 'SOURIS', '0.8m', '30.0kg', "Il doit garder sa queue en contact avec le sol pour éviter toute électrocution.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/026.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/026.wav'),
('027', 'SABELETTE', 'SOURIS', '0.6m', '12.0kg', "Il s'enterre dans les régions arides et désertiques. Il émerge seulement pour chasser.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/027.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/027.wav'),
('028', 'SABLAIREAU', 'SOURIS', '1.0m', '29.5kg', "Il se roule en boule hérissée de piques s'il est menacé. Il peut ainsi s'enfuir ou attaquer.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/028.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/028.wav'),
('029', 'NIDORAN♀', 'VENEPIC', '0.4m', '7.0kg', "Ne doit pas être confondu avec Nidoran♂.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/029.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/029.wav'),
('030', 'NIDORINA', 'VENEPIC', '0.8m', '20.0kg', "La corne de la femelle grandit lentement. Elle préfère attaquer avec ses griffes et sa gueule.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/030.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/030.wav'),
('031', 'NIDOQUEEN', 'PERCEUR', '1.3m', '60.0kg', "Ses écailles très résistantes et son corps massif sont des armes dévastatrices.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/031.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/031.wav'),
('032', 'NIDORAN♂', 'VENEPIC', '0.5m', '9.0kg', "Ne doit pas être confondu avec Nidoran♀.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/032.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/032.wav'),
('033', 'NIDORINO', 'VENEPIC', '0.9m', '19.5kg', "Très agressif, il est prompt à répondre à la violence. La corne sur sa tête est venimeuse.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/033.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/033.wav'),
('034', 'NIDOKING', 'PERCEUR', '1.4m', '62.0kg', "Sa queue est une arme redoutable, il s'en sert pour attraper sa proie et lui broyer les os.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/034.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/034.wav'),
('035', 'MELOFEE', 'FEE', '0.6m', '7.5kg', "Très recherché pour son aura mystique, il est très rare et ne vit que dans des endroits précis.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/035.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/035.wav'),
('036', 'MELODELFE', 'FEE', '1.3m', '40.0kg', "Une sorte de petite fée très rare. Il se cache en apercevant un être humain.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/036.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/036.wav'),
('037', 'GOUPIX', 'RENARD', '0.6m', '9.9kg', "Il n'a qu'une seule queue à la naissance. Celle-ci se divise à la pointe au fil des ans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/037.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/037.wav'),
('038', 'FEUNARD', 'RENARD', '1.1m', '19.9kg', "Très intelligent et rancunier. Attrapez-lui une de ses queues et il vous maudira pour 1000 ans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/038.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/038.wav'),
('039', 'RONDOUDOU', 'BOUBOULE', '0.5m', '5.5kg', "Quand ses yeux s'illuminent, il chante une mystérieuse berceuse.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/039.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/039.wav'),
('040', 'GRODOUDOU', 'BOUBOULE', '1.0m', '12.0kg', "En cas de danger, il gonfle d'air son corps doux et potelé dans des proportions gigantesques.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/040.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/040.wav'),
('041', 'NOSFERAPTI', 'CHOVSOURIS', '0.8m', '7.5kg', "Se déplace en colonie dans les endroits sombres. Il s'oriente grâce aux ultrasons.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/041.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/041.wav'),
('042', 'NOSFERALTO', 'CHOVSOURIS', '1.6m', '55.0kg', "Une fois son adversaire mordu, il absorbera son énergie même s'il est trop gros pour voler.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/042.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/042.wav'),
('043', 'MYSTHERBE', 'RACINE', '0.5m', '5.4kg', "Pendant la journée il se cache sous la terre. Il s'aventure la nuit pour planter des graines.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/043.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/043.wav'),
('044', 'ORTIDE', 'RACINE', '0.8m', '8.6kg', "Le liquide qui coule de sa bouche est comestible. Il sert à appâter sa proie.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/044.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/044.wav'),
('045', 'RAFFLESIA', 'FLEUR', '1.2m', '18.6kg', "Plus ses pétales son grands, plus ils contiennent de pollen toxique.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/045.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/045.wav'),
('046', 'PARAS', 'CHAMPIGNON', '0.3m', '5.4kg', "Les champignons sur son dos se nourrissent des nutriments de leur hôte insectoïde.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/046.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/046.wav'),
('047', 'PARASECT', 'CHAMPIGNON', '1.0m', '29.5kg', "Une symbiose entre un parasite et un insecte. Le champignon a pris le contrôle de son hôte.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/047.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/047.wav'),
('048', 'MIMITOSS', 'VERMINE', '1.0m', '30.0kg', "Il vit a l'ombre des grands arbres où il mange des insectes. il est attiré par la lumière.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/048.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/048.wav'),
('049', 'AEROMITE', 'PAPIPOISON', '1.5m', '12.5kg', "Les motifs ocres de ses ailes changent en fonction de son type de poison.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/049.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/049.wav'),
('050', 'TAUPIQUEUR', 'TAUPE', '0.2m', '0.8kg', "Il vit a un mètre sous la terre et se nourrit de racines. Il apparaît rarement à la surface.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/050.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/050.wav'),
('051', 'TRIOPIKEUR', 'TAUPE', '0.7m', '33.3kg', "Un groupe de Taupiqueur. Il crée des séismes en creusant à plus de 100 Km de profondeur.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/051.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/051.wav'),
('052', 'MIAOUSS', 'CHADEGOUT', '0.4m', '4.2kg', "Il adore les pièces de monnaie. Il hante les rues à la recherche de pièces oubliées par les passants.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/052.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/052.wav'),
('053', 'PERSIAN', 'CHADEVILLE', '1.0m', '32.0kg', "Très apprécié pour sa fourrure, il est difficile à apprivoiser en raison de son caractère rétif.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/053.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/053.wav'),
('054', 'PSYKOKWAK', 'CANARD', '0.8m', '19.6kg', "Il distrait ses ennemis avec des grimaces débiles et les attaque ensuite avec ses pouvoirs Psy.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/054.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/054.wav'),
('055', 'AKWAKWAK', 'CANARD', '1.7m', '76.6kg', "Il nage avec élégance le long des cotes. Il est souvent confondu avec le monstre japonais: Kappa.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/055.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/055.wav'),
('056', 'FEROSINGE', 'PORSINGE', '0.5m', '28.0kg', "Il se met en colère très vite. Calme ou furieux, son humeur change d'une seconde à l'autre.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/056.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/056.wav'),
('057', 'COLOSSINGE', 'PORSINGE', '1.0m', '32.0kg', "Agressif et teigneux, il poursuit son gibier jusqu'à épuisement complet.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/057.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/057.wav'),
('058', 'CANINOS', 'CHIOT', '0.7m', '19.0kg', "Pour protéger son territoire, il aboie et mord jusqu'à ce que les intrus s'enfuient.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/058.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/058.wav'),
('059', 'ARCANIN', 'LEGENDAIRE', '1.9m', '155.0kg', "Un Pokémon très recherché pour sa grâce légendaire. Son pas élégant semble glisser sur le vent.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/059.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/059.wav'),
('060', 'PTITARD', 'TETARD', '0.6m', '12.4kg', "Il court mal avec ses petites pattes. Il préfère nager que de se tenir debout.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/060.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/060.wav'),
('061', 'TETARTE', 'TETARD', '1.0m', '20.0kg', "Amphibie, il peut vivre à l'air libre mais il doit rester mouillé pour survivre.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/061.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/061.wav'),
('062', 'TARTARD', 'TETARD', '1.3m', '54.0kg', "Excellent nageur, il pratique le crawl ou la nage papillon mieux qu'un champion olympique.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/062.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/062.wav'),
('063', 'ABRA', 'PSY', '0.9m', '19.5kg', "Son don de télépathie lui permet de sentir le danger et de se TELEPORTER en un lieu sûr.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/063.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/063.wav'),
('064', 'KADABRA', 'PSY', '1.3m', '56.5kg', "Son corps émet des ondes alpha provoquant des migraines à ceux qui se trouvent à proximité.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/064.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/064.wav'),
('065', 'ALAKAZAM', 'PSY', '1.5m', '48.0kg', "Son super cerveau peut effectuer des opérations à la vitesse d'un ordinateur. Il a un Q.I. de 5000.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/065.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/065.wav'),
('066', 'MACHOC', 'COLOSSE', '0.8m', '19.5kg', "Il adore la musculation. Il pratique les arts martiaux pour devenir encore plus fort.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/066.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/066.wav'),
('067', 'MACHOPEUR', 'COLOSSE', '1.5m', '70.5kg', "Son corps est si puissant qu'il lui faut une ceinture de force pour équilibrer ses mouvements.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/067.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/067.wav'),
('068', 'MACKOGNEUR', 'COLOSSE', '1.6m', '130.0kg', "Ses coups de poings sont si puissants qu'ils font voler ses adversaires jusqu'à l'horizon.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/068.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/068.wav'),
('069', 'CHETIFLOR', 'FLEUR', '0.7m', '4.0kg', "Un Pokémon carnivore qui se nourrit de petits insectes. Ses racines servent d'attaches.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/069.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/069.wav'),
('070', 'BOUSTIFLOR', 'CARNIVORE', '1.0m', '6.4kg', "Il crache de la Poudre Toxik pour immobiliser sa proie et il l'achève avec de l'Acide.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/070.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/070.wav'),
('071', 'EMPIFLOR', 'CARNIVORE', '1.7m', '15.5kg', "Il vit en colonie dans la jungle mais personne n'en est jamais revenu vivant.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/071.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/071.wav'),
('072', 'TENTACOOL', 'MOLLUSQUE', '0.9m', '45.5kg', "Flottant au bord des cotes, les pêcheurs se font souvent arroser d'acide quand ils en accrochent un.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/072.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/072.wav'),
('073', 'TENTACRUEL', 'MOLLUSQUE', '1.6m', '55.0kg', "Ses tentacules sont rétractées au repos. En situation de chasse, ils rallongent.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/073.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/073.wav'),
('074', 'RACAILLOU', 'ROCHE', '0.4m', '20.0kg', "Il vit dans les plaines ou les montagnes. On le confond souvent avec un petit caillou.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/074.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/074.wav'),
('075', 'GRAVALANCH', 'ROCHE', '1.0m', '105.0kg', "Pour se déplacer il dégringole le long des pentes. Il pulvérise tout obstacle sur son passage.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/075.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/075.wav'),
('076', 'GROLEM', 'TITANESQUE', '1.4m', '300.0kg', "Son corps de pierre est indestructible. Il peut supporter des explosions de dynamite.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/076.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/076.wav'),
('077', 'PONYTA', 'CHEVAL FEU', '1.0m', '30.0kg', "Ses sabots sont plus résistants que le diamant. Il peut aplatir n'importe quoi en le piétinant.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/077.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/077.wav'),
('078', 'GALOPA', 'CHEVAL FEU', '1.7m', '95.0kg', "Doté d'un esprit de compétition, il poursuit toute créature rapide pour faire la course.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/078.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/078.wav'),
('079', 'RAMOLOSS', 'CRETIN', '1.2m', '36.0kg', "Très lent et endormi, il lui faut 5 secondes pour ressentir la douleur d'une attaque.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/079.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/079.wav'),
('080', 'FLAGADOSS', 'SYMBIOSE', '1.6m', '78.5kg', "Le Kokiyas attaché à la queue du Ramoloss se nourrit des restes de son hôte.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/080.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/080.wav'),
('081', 'MAGNETI', 'MAGNETIQUE', '0.3m', '6.0kg', "Il contrôle la gravité pour pouvoir voler. il attaque avec des Cage-Éclair.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/081.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/081.wav'),
('082', 'MAGNETON', 'MAGNETIQUE', '1.0m', '60.0kg', "Constitué de Magnéti reliés les uns aux autres, il apparaît lorsque le soleil brille.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/082.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/082.wav'),
('083', 'CANARTICHO', 'CANARD FOU', '0.8m', '15.0kg', "Il utilise l'oignon qu'il a dans la bouche comme une épée d'acier.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/083.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/083.wav'),
('084', 'DODUO', 'DUOISEAU', '1.4m', '39.2kg', "Cet oiseau vole très mal mais court très vite. Il laisse de gigantesques empreintes de pas.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/084.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/084.wav'),
('085', 'DODRIO', 'TRIOISEAU', '1.8m', '85.2kg', "Il élabore des plans complexes avec ses trois cerveaux. Une de ses têtes reste toujours éveillée.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/085.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/085.wav'),
('086', 'OTARIA', 'OTARIE', '1.1m', '90.0kg', "La corne sur son front est très résistante. Elle lui sert à percer des blocs de glace.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/086.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/086.wav'),
('087', 'LAMANTINE', 'OTARIE', '1.7m', '120.0kg', "Il emmagasine la chaleur dans son corps. Il peut nager dans l'eau glacée à plus de 8 noeuds.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/087.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/087.wav'),
('088', 'TADMORV', 'DEGUEU', '0.9m', '30.0kg', "Vivant dans des tas d'ordure, il se nourrit des déchets polluants rejetés par les usines.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/088.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/088.wav'),
('089', 'GROTADMORV', 'DEGUEU', '1.2m', '30.0kg', "Il est recouvert d'une épaisse couche toxique. Il laisse une trace empoisonnée derrière lui.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/089.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/089.wav'),
('090', 'KOKIYAS', 'BIVALVE', '0.3m', '4.0kg', "Protégé par une carapace très résistante, il est vulnérable quand celle-ci s'ouvre.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/090.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/090.wav'),
('091', 'CRUSTABRI', 'BIVALVE', '1.5m', '132.5kg', "Une fois menacé, il envoie de rapides volées de dards. Sa partie interne est inconnue.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/091.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/091.wav'),
('092', 'FANTOMINUS', 'GAZ', '1.3m', '0.1kg', "Ce Pokémon gazeux plonge ses victimes dans un profond sommeil sans qu'elles ne s'en aperçoivent.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/092.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/092.wav'),
('093', 'SPECTRUM', 'GAZ', '1.6m', '0.1kg', "Il peut se glisser à travers les murs comme une créature d'une autre dimension.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/093.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/093.wav'),
('094', 'ECTOPLASMA', 'OMBRE', '1.5m', '40.5kg', "Les nuits de pleine lune, il imite l'ombre des passants et se moque de leur effroi.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/094.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/094.wav'),
('095', 'ONIX', 'SERPENROC', '8.8m', '210.0kg', "Les parties en pierre de son corps durcissent pour devenir comme un diamant de couleur noire.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/095.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/095.wav'),
('096', 'SOPORIFIK', 'HYPNOSE', '1.0m', '32.4kg', "Il endort ses ennemis et dévore leurs songes. En mangeant de mauvais rêves, il devient malade.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/096.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/096.wav'),
('097', 'HYPNOMADE', 'HYPNOSE', '1.6m', '75.6kg', "En fixant son adversaire, il l'assaille avec les attaques psy d'hypnose et de Choc Mental.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/097.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/097.wav'),
('098', 'KRABBY', 'DOUX CRABE', '0.4m', '6.5kg', "Ses pinces sont des armes très puissantes. Elles lui servent aussi à garder son équilibre.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/098.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/098.wav'),
('099', 'KRABBOSS', 'PINCE', '1.3m', '60.0kg', "Son énorme pince peut déployer une pression de 1000 Kg. Mais elle est très encombrante.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/099.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/099.wav'),
('100', 'VOLTORBE', 'BALLE', '0.5m', '10.4kg', "Vivant dans les centrales, ce Pokémon survolté est souvent confondu avec une Poké Ball.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/100.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/100.wav'),
('101', 'ELECTRODE', 'BALLE', '1.2m', '66.6kg', "Il emmagasine des quantités énormes de courants électriques sous pression pouvant exploser.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/101.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/101.wav'),
('102', 'NOEUNOEUF', 'OEUF', '0.4m', '2.5kg', "Souvent pris pour des oeufs, ils attaquent en groupe comme un essaim.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/102.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/102.wav'),
('103', 'NOADKOKO', 'FRUITPALME', '2.0m', '120.0kg', "On raconte que si une de ses têtes se détache, elle se transforme en Noeunoeuf.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/103.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/103.wav'),
('104', 'OSSELAIT', 'SOLITAIRE', '0.4m', '6.5kg', "Il ne retire jamais son casque en os. Personne n'a jamais vu son vrai visage.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/104.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/104.wav'),
('105', 'OSSATUEUR', "GARD'OS", '1.0m', '45.0kg', "L'os qu'il tient dans sa main est une arme. Il peut le lancer avec adresse pour assommer sa proie.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/105.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/105.wav'),
('106', 'KICKLEE', 'LATTEUR', '1.5m', '49.8kg', "S'il est pressé, ses jambes s'allongent progressivement. Il court très rapidement.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/106.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/106.wav'),
('107', 'TYGNON', 'PUNCHEUR', '1.4m', '50.2kg', "Il distribue des séries de coups de poing rapide comme l'éclair, invisibles à l'oeil nu.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/107.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/107.wav'),
('108', 'EXCELANGUE', 'LECHEUR', '1.2m', '65.5kg', "Il peut projeter sa langue comme un caméléon. Tout contact avec elle produit une irritation.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/108.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/108.wav'),
('109', 'SMOGO', 'GAZ MORTEL', '0.6m', '1.0kg', "Son corps instable constitué de gaz toxiques peut exploser soudainement.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/109.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/109.wav'),
('110', 'SMOGOGO', 'GAZ MORTEL', '1.2m', '9.5kg', "Deux Smogo peuvent se combiner en un seul Smogogo en mélangeant leur gaz.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/110.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/110.wav'),
('111', 'RHINOCORNE', 'PIQUANT', '1.0m', '115.0kg', "Avec une ossature 1000 fois plus résistante que celle de l'homme, ses charges sont dévastatrices.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/111.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/111.wav'),
('112', 'RHINOFEROS', 'PERCEUR', '1.9m', '120.0kg', "Son épiderme très élevé lui permet de survivre dans un environnement de plus de 3600 degrés.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/112.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/112.wav'),
('113', 'LEVEINARD', 'OEUF', '1.1m', '34.6kg', "Un Pokémon rare et difficile à capturer qui porte chance et bien-être à son possesseur.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/113.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/113.wav'),
('114', 'SAQUEDENEU', 'VIGNE', '1.0m', '35.0kg', "Son corps est recouvert de lianes similaires à des algues. Elles bougent quand il marche.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/114.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/114.wav'),
('115', 'KANGOUREX', 'MATERNEL', '2.2m', '80.0kg', "Son enfant ne quitte la poche ventrale protectrice qu'à l'âge de 3 ans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/115.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/115.wav'),
('116', 'HYPOTREMPE', 'DRAGON', '0.4m', '8.0kg', "Réputé pour tirer avec précision sur des insectes volants à la surface de l'eau.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/116.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/116.wav'),
('117', 'HYPOCEAN', 'DRAGON', '1.2m', '25.0kg', "Il peut nager à l'envers en agitant ses petites nageoires pectorales.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/117.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/117.wav'),
('118', 'POISSIRENE', 'POISSON', '0.6m', '15.0kg', "Sa queue ondule gracieusement comme un voile. On l'appelle Reine des océans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/118.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/118.wav'),
('119', 'POISSOROY', 'POISSON', '1.3m', '39.0kg', "Pendant la saison des amours, on peut le voir nager près des rivières ou des lacs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/119.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/119.wav'),
('120', 'STARI', 'ETOILE', '0.8m', '34.5kg', "Un Pokémon bien curieux qui peut régénérer ses appendices sectionnés pendant un combat.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/120.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/120.wav'),
('121', 'STAROSS', 'MYSTERIEUX', '1.1m', '80.0kg', "Son coeur brille des couleurs de l'arc-en-ciel. On dit que c'est une pierre précieuse.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/121.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/121.wav'),
('122', 'M.MIME', 'BLOQUEUR', '1.3m', '54.5kg', "Dérangez-le pendant qu'il mime, et il vous distribuera une volée de claques.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/122.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/122.wav'),
('123', 'INSECATEUR', 'MANTE', '1.5m', '56.0kg', "Rapide et agile comme un ninja, il se déplace si vite qu'il crée l'illusion d'être en groupe.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/123.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/123.wav'),
('124', 'LIPPOUTOU', 'HUMANOIDE', '1.4m', '40.6kg', "Il ondule ses hanches en marchant et entraîne les gens dans des danses frénétiques.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/124.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/124.wav'),
('125', 'ELEKTEK', 'ELECTRIQUE', '1.1m', '30.0kg', "Vivant dans les centrales, il provoque des pannes de courant en s'aventurant en ville.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/125.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/125.wav'),
('126', 'MAGMAR', 'CRACHE-FEU', '1.3m', '44.5kg', "Son corps en fusion brûle d'une flamme orangée le rendant invisible dans le feu.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/126.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/126.wav'),
('127', 'SCARABRUTE', 'SCARABEE', '1.5m', '55.0kg', "Quand il ne peut écraser sa proie avec sa pince, il la secoue et l'envoie dans les airs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/127.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/127.wav'),
('128', 'TAUROS', 'BUFFLE', '1.4m', '88.4kg', "Une fois sa cible en vue, il la charge furieusement en fouettant l'air de sa queue.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/128.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/128.wav'),
('129', 'MAGICARPE', 'POISSON', '0.9m', '10.0kg', "Autrefois, il était beaucoup plus puissant que cette créature minablement faible.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/129.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/129.wav'),
('130', 'LEVIATOR', 'TERRIFIANT', '6.5m', '235.0kg', "Gigantesque et maléfique, il est capable de raser une ville entière dans un accès de rage.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/130.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/130.wav'),
('131', 'LOKHLASS', 'TRANSPORT', '2.5m', '220.0kg', "Ce Pokémon en voie d'extinction peut transporter des passagers sur son dos par-delà les océans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/131.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/131.wav'),
('132', 'METAMORPH', 'MORPHING', '0.3m', '4.0kg', "Il est capable de copier le code génétique d'un ennemi pour se transformer en son double.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/132.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/132.wav'),
('133', 'EVOLI', 'EVOLUTIF', '0.3m', '6.5kg', "Ce mystérieux Pokémon peut évoluer de différentes façons grâce à des pierres.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/133.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/133.wav'),
('134', 'AQUALI', 'BULLEUR', '1.0m', '29.0kg', "Il vit au bord de l'eau. Sa queue lui donne l'apparence d'une sirène.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/134.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/134.wav'),
('135', 'VOLTALI', 'ORAGE', '0.8m', '24.5kg', "Il se charge d'électricité statique pour envoyer des décharges de 1000 volts.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/135.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/135.wav'),
('136', 'PYROLI', 'FLAMME', '0.9m', '25.0kg', "Il peut accumuler suffisamment de chaleur pour atteindre des températures de 1 600 degrés.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/136.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/136.wav'),
('137', 'PORYGON', 'VIRTUEL', '0.8m', '36.5kg', "Un Pokémon fait de programmes et d'algorithmes. Il peut survivre en milieu virtuel.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/137.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/137.wav'),
('138', 'AMONITA', 'SPIRALE', '0.4m', '7.5kg', "Disparu depuis longtemps, il peut être réanimé génétiquement à partir d'anciens fossiles.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/138.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/138.wav'),
('139', 'AMONISTAR', 'SPIRALE', '1.0m', '35.0kg', "Un Pokémon préhistorique qui disparut quand sa coquille devint trop lourde à déplacer.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/139.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/139.wav'),
('140', 'KABUTO', 'CARAPACE', '0.5m', '11.5kg', "Un Pokémon reconstitué à partir d'un fossile trouvé sur un site préhistorique.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/140.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/140.wav'),
('141', 'KABUTOPS', 'CARAPACE', '1.3m', '40.5kg', "Sa forme élancée lui permet de nager rapidement. Il lacère sa proie avant d'en absorber la vie.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/141.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/141.wav'),
('142', 'PTERA', 'FOSSILE', '1.8m', '59.0kg', "Un Pokémon préhistorique qui attaque son ennemi à la gorge avec ses crocs acérés.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/142.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/142.wav'),
('143', 'RONFLEX', 'PIONCEUR', '2.1m', '460.0kg', "Très paresseux, il ne fait que manger et dormir. Plus il est gros, plus il devient fainéant.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/143.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/143.wav'),
('144', 'ARTIKODIN', 'GLACIAIRE', '1.7m', '55.4kg', "Le légendaire oiseau des glaces. On dit qu'il apparaît aux gens perdus dans les sommets.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/144.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/144.wav'),
('145', 'ELECTHOR', 'ELECTRIQUE', '1.6m', '52.6kg', "L'oiseau légendaire de la foudre. Il surgit hors des nuages en lançant d'énormes éclairs.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/145.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/145.wav'),
('146', 'SULFURA', 'FLAMME', '2.0m', '60.0kg', "Le légendaire oiseau de feu. Une pluie de flammes surgit à chaque battement de ses ailes.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/146.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/146.wav'),
('147', 'MINIDRACO', 'DRAGON', '1.8m', '3.3kg', "Longtemps considéré comme légendaire, une colonie fut découverte dans les océans.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/147.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/147.wav'),
('148', 'DRACO', 'DRAGON', '4.0m', '16.5kg', "Un Pokémon légendaire plein de charme. Il peut contrôler les variations climatiques.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/148.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/148.wav'),
('149', 'DRACOLOSSE', 'DRAGON', '2.2m', '210.0kg', "Un Pokémon marin extrêmement rare. On dit qu'il est aussi intelligent que l'homme.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/149.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/149.wav'),
('150', 'MEWTWO', 'GENETIQUE', '2.0m', '122.0kg', "Il est le fruit de nombreuses expériences génétiques horribles et malsaines.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/150.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/150.wav'),
('151', 'MEW', 'NOUVEAU', '0.4m', '4.0kg', "Unique et rare, son existence est remise en cause par les experts. Peu nombreux sont ceux qui l'ont vu.", '/Users/fnk/PycharmProjects/Pokedex/src/sprites/151.png', '/Users/fnk/PycharmProjects/Pokedex/src/sound/151.wav')]


# DATABASE CREATION ----------------------------

db = sqlite3.connect('pokedex.db')
c = db.cursor()

#c.execute("""CREATE TABLE Kanto (
#    PK_Index INTEGER PRIMARY KEY AUTOINCREMENT,
#    Pokemon_Index TEXT,
#    Pokemon_Name VARCHAR(50),
#    Pokemon_Category VARCHAR(50),
#    Pokemon_Height VARCHAR(10),
#    Pokemon_Weight VARCHAR(10),
#    Pokemon_Description TEXT,
#    Pokemon_SpritePath TEXT,
#    Pokemon_CryPath TEXT
#);""")

c.executemany('INSERT INTO Kanto (Pokemon_Index, Pokemon_Name, Pokemon_Category, Pokemon_Height, Pokemon_Weight, Pokemon_Description, Pokemon_SpritePath, Pokemon_CryPath) VALUES (?,?,?,?,?,?,?,?)', pokedex_data)


# TKINTER CONFIGURATION -----------------------

root = tkb.Window(title='Pokédex', resizable=(tkb.NO, tkb.NO))
#root.geometry("350x370+1000+150") #definitive
root.geometry("350x440+1000+150") #temporary

ico = Image.open('/Users/fnk/PycharmProjects/Pokedex/src/sprites/appicon.png')
appicon = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, appicon)

pyglet.font.add_file('/Users/fnk/PycharmProjects/Pokedex/src/pokemon.ttf')


# ENGINE -------------------------------------

c.execute("SELECT * FROM Kanto")
data = c.fetchall()
rows_nb = 0
for rows in data:
    rows_nb += 1

index = rows_nb
current_index = 0
sv_search = tkb.StringVar(value="")
sv_pokemon_index = tkb.StringVar(value="001")
sv_pokemon_name = tkb.StringVar(value="BULBIZARRE")
sv_pokemon_category = tkb.StringVar(value="GRAINE")
sv_pokemon_height = tkb.StringVar(value="0.7m")
sv_pokemon_weight = tkb.StringVar(value="6.9kg")
sv_pokemon_description = tkb.StringVar(value="Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance.")
sv_pokemon_spritepath = tkb.StringVar(value="/Users/fnk/PycharmProjects/Pokedex/src/sprites/001.png")
sv_pokemon_crypath = tkb.StringVar(value="/Users/fnk/PycharmProjects/Pokedex/src/sound/001.wav")
music_playing = 1


def caps(event):
    sv_search.set(sv_search.get().upper())


def key_return(event):
    search()


def key_left(event):
    go_previous()


def key_right(event):
    go_next()


def display(index):
    global current_index
    if 0 <= index < rows_nb:
        current_entry = data[index]
        sv_pokemon_index.set(current_entry[1])
        sv_pokemon_name.set(current_entry[2])
        sv_pokemon_category.set(current_entry[3])
        sv_pokemon_height.set(current_entry[4])
        sv_pokemon_weight.set(current_entry[5])
        sv_pokemon_description.set(current_entry[6])
        sv_pokemon_spritepath.set(current_entry[7])
        sv_pokemon_crypath.set(current_entry[8])
        display_sprite()
        current_index = index


def display_sprite():
    pokemon_img = Image.open(sv_pokemon_spritepath.get())
    pokemon_imgsize = pokemon_img.resize((100, 100))
    pokemon_imgpi = ImageTk.PhotoImage(pokemon_imgsize)
    pokemon_sprite = tkb.Label(root, image=pokemon_imgpi)
    pokemon_sprite.image = pokemon_imgpi
    pokemon_sprite.place(x=45, y=10)


def go_previous():
    global current_index
    if current_index > 0:
        current_index -= 1
        display(current_index)
    else:
        current_index = 0
        display(current_index)


def go_next():
    global current_index
    if current_index < rows_nb - 1:
        current_index += 1
        display(current_index)


def char_limit(*args):
    limit = sv_search.get()
    if len(limit) > 10:
        sv_search.set(limit[:10])


sv_search.trace('w', char_limit)


def search():
    c.execute("SELECT * FROM Kanto WHERE Pokemon_Name = '{}'".format(sv_search.get()))
    result = c.fetchone()
    if result is not None:
        pk_index = result[0]-1
        display(pk_index)
    else:
        sv_search.set("NO DATA")


def play_cry(event):
    cry_path = pygame.mixer.Sound(sv_pokemon_crypath.get())
    cry_path.play()
    cry_length = cry_path.get_length()
    print(cry_length)
    pygame.mixer.music.set_volume(0)
    sleep(cry_length)
    pygame.mixer.music.set_volume(100)


def show_zone(event):
    print("zone")


def music_toggle(event):
    global music_playing, icn_m_toggle
    if music_playing == 1:
        stop_music()
        icn_m_toggle_src['file'] = "/Users/fnk/PycharmProjects/Pokedex/src/sprites/play.png"
        music_playing = 0
    elif music_playing == 0:
        play_music()
        icn_m_toggle_src['file'] = "/Users/fnk/PycharmProjects/Pokedex/src/sprites/stop.png"
        music_playing = 1


def play_music():
    bg_music = '/Users/fnk/PycharmProjects/Pokedex/src/sound/bg_music.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(open(bg_music))
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()


# USER INTERFACE ------------------------------

# POKEMON DATA DISPLAY ------------------------

pokemon_name = tkb.Label(root, textvariable=sv_pokemon_name, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_name.place(x=175, y=5)

pokemon_category = tkb.Label(root, textvariable=sv_pokemon_category, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_category.place(x=175, y=40)

pokemon_height_lbl = tkb.Label(root, text='TAI', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_height_lbl.place(x=175, y=75)

pokemon_height = tkb.Label(root, textvariable=sv_pokemon_height, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_height.place(x=240, y=75)

pokemon_weight_lbl = tkb.Label(root, text='PDS', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_weight_lbl.place(x=175, y=110)

pokemon_weight = tkb.Label(root, textvariable=sv_pokemon_weight, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
pokemon_weight.place(x=240, y=110)

display_sprite()

index_img = Image.open('/Users/fnk/PycharmProjects/Pokedex/src/sprites/no.png')
index_imgsize = index_img.resize((16, 16))
index_imgpi = ImageTk.PhotoImage(index_imgsize)
index_sprite = tkb.Label(root, image=index_imgpi)
index_sprite.image = index_imgpi
index_sprite.place(x=50, y=123)

pokemon_index_lbl = tkb.Label(root, text='.', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 24))
pokemon_index_lbl.place(x=70, y=115)

pokemon_index = tkb.Label(root, textvariable=sv_pokemon_index, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
pokemon_index.place(x=90, y=112)

pokemon_description = tkb.Label(root, textvariable=sv_pokemon_description, wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
pokemon_description.place(x=15, y=170)

separator1_img = Image.open('/Users/fnk/PycharmProjects/Pokedex/src/sprites/separator.png')
separator1_imgsize = separator1_img.resize((350, 14))
separator1_imgpi = ImageTk.PhotoImage(separator1_imgsize)
separator1_sprite = tkb.Label(root, image=separator1_imgpi)
separator1_sprite.image = separator1_imgpi
separator1_sprite.place(x=0, y=150)

separator2_img = Image.open('/Users/fnk/PycharmProjects/Pokedex/src/sprites/separator.png')
separator2_imgsize = separator2_img.resize((350, 14))
separator2_imgpi = ImageTk.PhotoImage(separator2_imgsize)
separator2_sprite = tkb.Label(root, image=separator2_imgpi)
separator2_sprite.image = separator2_imgpi
separator2_sprite.place(x=0, y=333)


# OPTIONS, SEARCH & NAVIGATION -------------------------

icn_m_toggle_src = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/stop.png')
icn_m_toggle = tkb.Label(root, image=icn_m_toggle_src)
icn_m_toggle.place(x=10, y=10, width=24, height=24)
icn_m_toggle.bind("<Button-1>", music_toggle)

south_search = tkb.Label(root, text='RECHERCHE', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
south_search.place(x=15, y=350)
icn_search = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/search.png')
btn_search = tk.Button(root, image=icn_search, autostyle=False, command=search)
btn_search.place(x=160, y=365, width=16, height=16)
root.bind("<Return>", key_return)
en_search = tkb.Entry(root, textvariable=sv_search, bootstyle='dark', state="normal", font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
en_search.place(x=15, y=385, width=170, height=40)
en_search.bind("<KeyRelease>", caps)

icn_previous = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/previous.png')
btn_previous = tk.Button(root, image=icn_previous, autostyle=False, command=go_previous)
btn_previous.place(x=200, y=365, width=16, height=16)
root.bind("<Left>", key_left)
south_nav = tkb.Label(root, text='NAVIG.', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
south_nav.place(x=225, y=350)
icn_next = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/next.png')
btn_next = tk.Button(root, image=icn_next, autostyle=False, command=go_next)
btn_next.place(x=320, y=365, width=16, height=16)
root.bind("<Right>", key_right)
btn_cry = tkb.Label(root, text='CRI', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
btn_cry.place(x=200, y=388)
btn_cry.bind("<Button-1>", play_cry)
btn_zone = tkb.Label(root, text='ZONE', font=('Pokémon Red/Blue/Green/Yellow Edition Font', 30))
btn_zone.place(x=270, y=388)
btn_zone.bind("<Button-1>", show_zone)


# MAIN ----------------------------------------

if __name__ == '__main__':
    play_music()
    root.mainloop()  # Start of program