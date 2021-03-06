from app import app, db
from models.user import User
from models.likes import Like
from models.dislikes import Dislike
from models.matches import Match


with app.app_context():
    db.drop_all()
    db.create_all()

    lara=User(
    email="lara@lara.com",
        first_name="lara",
        last_name="lara",
        password="C0r0naKaren",
    dob="1994-12-18",
    gender="female",
    gender_pref = "male",
    age_pref_max = 29,
    age_pref_min = 22,
    image_1 = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png',
    # has_seen = [2]
    )

    laura=User(
    email="laura@laura.com",
        first_name="laura",
        last_name="laura",
        password="C0r0naKaren",
    dob="1994-12-18",
    gender="female"

    )

    karen=User(
    email="karen@karen.com",
        first_name="karen",
        last_name="karen",
        password="C0r0naKaren",
    dob="1994-12-18",
    gender="female",
    image_1="https://thehomeschoolresourceroom.com/wp-content/uploads/2017/04/social-media-2.jpg"
    )

    megan=User(
    email="megan@megan.com",
        first_name="megan",
        last_name="megan",
        password="C0r0naKaren",
    dob="1994-12-18",
    gender="female",
    image_1="https://static.billboard.com/files/2020/05/megan-thee-stallion-press-cr-emilio-coochie-2020-znj-billboard-1548-1590588553-1024x677.jpg",
    bio="Hot girl bummer"
    )

    alison=User(
    email="alison@alison.com",
        first_name="alison",
        last_name="alison",
        password="C0r0naKaren",
    dob="1994-12-18",
    gender="female",
    image_1="https://www.hklaw.com/-/media/images/professionals/w/walker-karen-d/walker-karen-d.jpg",
    bio="Shaikh the Flake"
    )

    shaikh=User(
    email="shaikh@shaikh.com",
        first_name="shaikh",
        last_name="shaikh",
        password="Shaikh123123",
    dob="1993-11-30",
    gender="male",
    gender_pref = "female",
    age_pref_max = 29,
    age_pref_min = 22,
    image_1 = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png'
    )

    ali=User(
    email="ali@ali.com",
        first_name="ali",
        last_name="ali",
        password="AliAli123",
    dob="1996-09-21",
    gender="male",
    gender_pref = "female",
    age_pref_max = 29,
    age_pref_min = 22,
    image_1 = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png',

    )

    like_1=Like(
    # id=1,
    liker_id=4,
    liked_id=3
    )

    like_2=Like(
    liker_id=6,
    liked_id=3
    )

    like_3=Like(
    liker_id=7,
    liked_id=3
    )

    # match_1=Match(
    #   user_1_id= 2,
    #   user_2_id=3
    # )



    # image_1=Images(
    #   image_1 = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png',
    #   user_id = 1
    # )

    # image_2=Images(
    #   image_1 = 'https://pbs.twimg.com/profile_images/1072898126128779264/YzGnrGa4_400x400.jpg',
    #   user_id = 2
    # )

    # image_3=Images(
    #   image_1='https://i.insider.com/5f1f25883f7370509a6d46d8?width=879&format=jpeg',
    #   user_id=3
    # )



    # db.session.add(dislike_1)
    db.session.add(lara)
    db.session.add(shaikh)
    db.session.add(ali)
    db.session.add(laura)
    db.session.add(karen)
    db.session.add(alison)
    db.session.add(megan)
    db.session.commit()

    db.session.add(like_1)
    db.session.add(like_2)
    db.session.add(like_3)

    # db.session.add(match_1)


    # db.session.add(image_1)
    # db.session.add(image_2)
    # db.session.add(image_3)

    db.session.commit()

