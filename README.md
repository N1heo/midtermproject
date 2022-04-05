# This is my midterm project

## Credits
The code foundation I took from my teacher's implementation of **Conway's game of life.**
The idea I overheard from my friend, that was doing something simillar years ago. All what I heard from him was: "I was making some kind of a human organism cellural simulation." After some time of working on this project, I found out that my teacher also mentioned this idea, but in the other group.

## The idea itself
So I've developed the idea into this:
- We have 3 kind of cells - white erythrocytes, bacteria and viruses. 
- The red background is blood, where everything is circulling.
- The white cells absorb all the bacteria and viruses. But with time, some new viruses and bacteria appear. All of that happening in some kind of a loop.
</a>

### Сoncept art, that I made in the beggining:

![dasdasda](https://user-images.githubusercontent.com/96371464/161592696-4a0e277d-57cc-4d35-bb5d-27cb671bf801.png)

### And how the simulation looks:

![Capture1](https://user-images.githubusercontent.com/96371464/161593121-399a5003-2477-4990-867b-6c84641ebd0e.PNG)

![Capture222](https://user-images.githubusercontent.com/96371464/161748590-3ea59143-bdee-4cbe-98b8-d9d7006a8f5d.PNG)

## Working procces
### Presets
Well, I started by adding preset function. I did that using tkinter **bind** method.
The user can add or delete all the 3 kind of cells using his mouse.
After that, I made it possible to start or stop the game, so user could make presets without sells dying immediately.

**Letting the user know, what to press is important:**

![Capture21](https://user-images.githubusercontent.com/96371464/161592851-9779baa6-3e75-426b-910e-78997074f3a3.PNG)

### Fixes
Making some tests, i find out that the game doesn't behave like conway's, there was a mistake in the sum line. After fixing it and having completely working _game of life_ I started to work on **my own rules** of the game.

## The code rules
This was the hardest part of the project. I had something like 10 versions of main algoritm and there was this problem. If I made them kind of a logical, then the visualization gets worster and to make it look better, I used a little bit more unlogical algrotims. So, here they are:
- If there is more than 6 bacteria or viruses around the white cell, it dies
- If there is only white cells around any cell, randomly or viruses or bacteria appear in the cell.
- Otherwise of all above, the white cells are growing.
</a>

## Exceptions
```       
try:
    if self.running is True:
        self.__step()
except AttributeError:
    pass
self.c.after(500, self.__draw)
```
I use this one for letting the simulation start, without declaring running = True in the beginning. Because of the loop, it will be always true, if I'll declare it at the beginning.

## Private methods
I changed the `__draw` and `__step` methods to private ones and `__b=[]` matrix variable because I need them only inside of the class.

## Code linting
Speaking of it, if you will copy the code directly from the github overview and paste it in the site, there gonna be 1 error, about the empty line in the end of the code. But that because overview simply don't show that line.

![Capture12](https://user-images.githubusercontent.com/96371464/161601709-86394b46-cb92-41d8-b57e-3e08411b91f2.PNG)

# End of the README

![mZLE3Cia2bk](https://user-images.githubusercontent.com/96371464/161602585-2238abb3-b559-4d90-9233-6734ee336b9b.png)

