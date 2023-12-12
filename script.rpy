# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Dr. Dino",color="#bb2727")

define f = Character("Dr. Nethropod",color="#bb7327")
define g = Character("Dr. Maniraptora",color="#bbb427")
define h = Character("Dr. Ornithomimidae",color="#31bb27")
define i = Character("Dr. Sauropod",color="#27bb5b")
define j = Character("Dr. Ceratopsian",color="#27bbb1")
define k = Character("Dr. Thyreophora",color="#0b9eee")
define l = Character("Dr. Pterosaur",color="#4027bb")
define m = Character("Dr. Tentanurae",color="#7d27bb")
define n = Character("Dr. Tyrannosauridae",color="#bb27b4")
define o = Character("Dr. Ornithopod",color="#bb276f")
define p = Character("Dr. Marine",color="#bb272c")

image dr dino = "dr dino.png"
 
#images used 
image ceratosaurus =  "Ceratosaurus.jpg" 
image carnotaurus = "Carnotaurus.jpg"
image dilophosaurus = "Dilophosaurus.jpg"
image megalosaurus =  "Megalosaurus.jpg" 
image gigantosaurus = "Gigantosaurus.jpg"
image allosaurus = "Allosaurus.jpg"
image velociraptor =  "Velociraptor.jpg" 
image microrapter = "Microraptor.jpg"
image therizinosaurus = "Therizinosaurus.jpg"
image gallimimus = "Gallimimus.jpg"
image ornithomimus = "Ornithomimus.jpg"
image pachycephalosaurus =  "Pachycephalosaurus.jpg" 
image eotyrannus =  "Eotyrannus.jpg" 
image tyrannosaurus = "Tyrannosaurus.jpg"
image tarbosaurus = "Tarbosaurus.jpg"
image diplodocus =  "Diplodocus.jpg" 
image brontosaurus = "Brontosaurus.jpg"
image brachiosaurus = "Brachiosaurus.jpg"
image titanosaurus = "Titanosaurus.jpg"
image triceratops = "Triceratops.jpg"
image protoceratops = "Protoceratops.jpg"
image styracosaurus = "Styracosaurus.jpg"
image parasaurolophus = "Parasaurolophus.jpg"
image hypsolophodon = "Hypsolophodon.jpg" 
image iguanodon = "Iguanodon.jpg"
image ankylosaurus = "Iguanodon.jpg"
image stegosaurus = "Stegosaurus.jpg"
image pterodactyl = "Pterodactyl.jpg"
image pteranodon = "Pteranodon.jpg"
image quetzalcoatlus = "Quetzalcoatlus.jpg"
image spinosaurus = "Suetzalcoatlus.jpg"
image plesiosaur = "Puetzalcoatlus.jpg"
image baryonyx = "Baryonyx.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dino museum

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at left:

    # These display lines of dialogue.

    e "Welcome to the museum!"

    e "I am Dr. Dino! I'll be happy to assist you."

    e "Do you need help identifying a dinosaur?"

    menu:

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

label choice1_yes:

    $ menu_flag = True

    e "Great! Let's get started."

    scene 199

    jump flight

label choice1_no:

    $ menu_flag = False

    e "okay, I'll be here if you need me!"

    jump choice1_done

label flight:
    show eileen happy at left:
 
    e "Does your dinosaur fly?"

    menu:
        "Yes! My dinosaur can fly.":
            jump pterosaur 
        "The Dinosaur I'm thinking of cannot fly.":
            jump swim 

label swim:
 
    e "Does your dinosaur swim?"

    menu:
        "Yes! My dinosaur can swim.":
            jump swimmers 
        "The Dinosaur I'm thinking of cannot swim.":
            jump herbivorous


label herbivorous:
    e "Is your dinosaur an herbivore?"

    menu:
        "Yes! My dinosaur is an herbivore.":
            jump long_necked 
        "The Dinosaur I'm thinking of is not an herbivore.":
            jump three_toed 

label three_toed:
    e "Is your dinosaur three toed?"

    menu:
        "Yes! My dinosaur is three toed.":
            jump netheropod 
        "The Dinosaur I'm thinking of is not three toed":
            jump stiff_tailed

label stiff_tailed:
    e "Does your dinosaur have a stiff tail?"

    menu:
        "Yes! My dinosaur has a stiff tail.":
            jump tentanurae  
        "The Dinosaur I'm thinking of does not have a stiff tail":
            jump elongated_arms

label elongated_arms:
    e "Does your dinosaur have elongated arms?"

    menu:
        "Yes! My dinosaur has elongated arms.":
            jump ostrich 
        "The Dinosaur I'm thinking of does not have elongated arms.":
            jump tyrannosauridae

label ostrich:
    e "Does your dinosaur have an ostrich-like appearance?"

    menu:
        "Yes! My dinosaur has an ostrich-like appearance.":
            jump ornithomimidae
        "The Dinosaur I'm thinking of does not have an ostrich-like appearance.":
            jump maniraptora

label long_necked:
    e "Does your dinosaur have a long neck?"
    
    menu:
        "Yes! My dinosaur has a long neck.":
            jump sauropods  
        "The Dinosaur I'm thinking of does not have a long neck.":
            jump armored 

label armored:
    e "Is your dinosaur armored?"

    menu:
        "Yes! My dinosaur is armored.":
            jump horns_and_frills   
        "The Dinosaur I'm thinking of is not armored.":
            jump choice1_done # figure out  

label horns_and_frills:
    e "Does your dinosaur have horns and/or bony frills?"

    menu:
        "Yes! My dinosaur has horns and/or bony frills.":
            jump ceratopsian   
        "The Dinosaur I'm thinking of does not have horns and/or bony frills.":
            jump bipedal

label bipedal:
    e "Does your dinosaur walk on 2 legs?"

    menu:
        "Yes! My dinosaur walks on 2 legs.":
            jump ornithopods   
        "The Dinosaur I'm thinking of does not walk on two legs.":
            jump thyreophora


label pterosaur:
    hide eileen happy 
    show dr dino at right
    menu:
        "Pteradactyl":
            show pterodactyl at truecenter:
            l "The Pterodactyl is considered the largest flying animal that ever lived at over 36 feet."
            l "This species went extinct in the late Cretaceous time period."
            jump choice1_done
        "Pteranodon":
            show pteranodon at truecenter:
            l "The Pteranodon lived in big flocks"
            l "This species went extinct in the Late Cretaceous"
            jump choice1_done
        "Quetzalcoatlus":
            show quetzalcoatlus at truecenter:
            l "The Quetzalcoatlus could fly down and scoop up small dinosaurs, just like pelicans do with fish."
            l "This species went extinct in the Late Cretaceous"
            jump choice1_done

label netheropod:
    hide eileen happy 
    show dr dino at right
    menu:
        "Ceratosaurus":
            show ceratosaurus at truecenter:
            f "The Deratosaurus is the only known dinosaur from the triceratops family to eat fish."
            f "This species went extinct in the Late Jurassic."
            jump choice1_done
        "Carnotaurus":
            show carnotaurus at truecenter:
            f "The Carnotaurus is the only species in the Theropoda group to have horns above their eyes."
            f " This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Dilophosaurus":
            show dilophosaurus at truecenter:
            f "In Jurassic Park, the Dilophosaurus is depicted as having an expandable frill and spitting poison. However, none of that is true, causing it to be the most misunderstood dinosaur that ever lived."
            f "This species went extinct in the Early Jurassic."
            jump choice1_done


label tentanurae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Megalosaurus":
            show megalosaurus at truecenter:
            m "The Megalosaurus could replace broken or missing teeth."
            m "This species went extinct in the Middle Jurassic."
            jump choice1_done
        "Gigantosaurus":
            show gigantosaurus at truecenter:
            m "The Gigantosaurus's brains had the approximate shape and weight of a banana"
            m "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Allosaurus":
            show allosaurus at truecenter:
            m "The Allosaurus " #incomplete 
            jump choice1_done

label maniraptora:
    hide eileen happy 
    show dr dino at right
    menu:
        "Velociraptor":
            show velociraptor at truecenter:
            g "The Velociraptor had feathers and was the size of a wolf."
            g "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Microraptor":
            show microraptor at truecenter:
            g "The Microraptor used its wings for gliding, not flying."
            g "This species went extinct in the Early Cretaceous"
            jump choice1_done
        "Therizinosaurus":
            show therizinosaurus at truecenter:
            g "The Therizinosaurus's claws were over 3 feet long."
            g "This species went extinct in the Late Cretaceous."
            jump choice1_done
            
label ornithomimidae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Gallimimus":
            show gallimimus at truecenter:
            h "The Gallimimus had a brain the size of a golf ball despite being 3 times taller than an average human."
            h "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Ornithomimus":
            show ornithomimus at truecenter:
            h "The Ornithomimus could run up to 50 miles per hour."
            h "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Pachycephalosaurus":
            show pachycephalosaurus at truecenter:
            h "The diameter of a Pachycephalosaurus' domed head could measure up to 2 feet."
            h "This species went extinct in the Late Cretaceous"
            jump choice1_done

label tyrannosauridae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Eotyrannus":
            show eotyrannus at truecenter:
            n "The Eotyrannus is known as the 'early tyrant' and the early relative to the T-Rex."
            n "This species went extinct in the Early Cretaceous."
            jump choice1_done
        "Tyrannosaurus":
            show tyrannosaurus at truecenter:
            n"The Tyrannosaurus could eat up to 500 pounds in one bite."
            n "This species went extinct in the Upper Cretaceous."
            jump choice1_done
        "Tarbosaurus":
            show tarbosaurus at truecenter:
            n"The Tarbosaurus has the smallest arms of any dinosaur relative to their body size."
            n "This species went extinct in the Late Cretaceous."
            jump choice1_done

label sauropods:
    hide eileen happy 
    show dr dino at right
    menu:
        "Diplodocus":
            show diplodocus at truecenter:
            i "The Diplodocus's front legs were shorter than their hind legs."
            i "This species went extinct in the Upper Jurassic."
            jump choice1_done
        "Brontosaurus":
            show brontosaurus at truecenter:
            i "The Brontosaurus could live up to 100 years."
            i "This species went extinct in the Late Jurassic."
            jump choice1_done
        "Brachiosaurus":
            show brachiosaurus at truecenter:
            i "The Brachiosaurus ate about 440 pounds per day."
            i "This species went extinct in the Late Jurassic."
            jump choice1_done
        "Titanosaurus":
            show titanosaurus at truecenter:
            i "The Titanosaurus could weigh up to 76 tons."
            i "This species went extinct in the Upper Cretaceous."
            jump choice1_done

label ceratopsian:
    hide eileen happy 
    show dr dino at right
    menu:
        "Triceratops":
            show triceratops at truecenter:
            j "The triceratops' horns changed as it grew."
            j "This species went extinct in the Upper Cretaceous."
            jump choice1_done
        "Protoceratops":
            show protoceratops at truecenter:
            j "The Protoceratops had four legs, but could walk on 2."
            j "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Stryacosaurus":
            show styracosaurus at truecenter:
            j "The Stryacosaurus could have anywhere from 4-6 horns."
            j "This species went extinct in the Late Cretaceous."
            jump choice1_done

label ornithopods:
    hide eileen happy 
    show dr dino at right
    menu:
        "Parasaurolophus":
            show parasaurolophus at truecenter:
            o "The Parasaurolophus's crest on its head allowed it to make loud trumpeting calls."
            o "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Hypsolophodon":
            show hypsolophodon at truecenter:
            o "The Hypsolophodon liked to chew its food and developed cheekbones."
            o "This species went extinct in the Early Cretaceous."
            jump choice1_done
        "Iguanodon":
            show iguanodon at truecenter:
            o "The Iguanodon had five fingers, but instead of thumbs they had a few fingers."
            o "This species went extinct in the Early Cretaceous."
            jump choice1_done

label thyreophora:
    hide eileen happy 
    show dr dino at right
    menu:
        "Ankylosaurus":
            show triceratops at truecenter:
            k "The Ankylosaurus's spikes on its head/body were strong enough to break teeth."
            k "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Stegosaurus":
            show stegosaurus at truecenter:
            k "The Stegosaurus is the state dinosaur of Colorado"
            k "This species went extinct in the Late Jurassic"
            jump choice1_done

label swimmers:
    hide eileen happy 
    show dr dino at right
    menu:
        "Spinosaurus":
            show spinosaurus at truecenter:
            k "The Spinosaurus was the biggest predator to ever walk the earth with a length of up to 60 feet."
            k "This species went extinct in the Late Cretaceous."
            jump choice1_done
        "Plesiosaur":
            show plesiosaur at truecenter:
            k "The Plesiosaur had possibly the strongest bite force of any animal at 33000 psi."
            k "This species went extinct in the Late Cretaceous"
            jump choice1_done
        "Baryonyx":
            show baryonyx at truecenter:
            k "The Baryonyx's jaw is designed to keep prey from wiggling free."
            k "This species went extinct in the Early Cretaceous."
            jump choice1_done
    

label choice1_done:
    hide dr dino
    show eileen happy at left
    scene dino museum
    e "Do you have another dinosaur you'd like to identify?"
    menu:
        "Yes!":
            jump flight
        "No, thanks!":
            jump end 

label end:
    e "I hope that helped. See you soon!"

    # This ends the game.

    return
