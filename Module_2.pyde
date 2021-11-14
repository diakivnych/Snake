import random
import math


class Geometry:
    # Геометрія
    @staticmethod
    def sqr(x):
        return x * x
    
    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt(Geometry.sqr(x2 - x1) + Geometry.sqr(y2 - y1))


class Info:
    score = 0
    size_ = 0
    life = 200
    sz_apples = 1
    cnt_apples = 1
        
    @classmethod
    def inc(cls):
        cls.score += 5
    
    @classmethod
    def inc_cnt_apples(cls):
        cls.sz_apples *= 2
        cls.cnt_apples += cls.sz_apples


class Apple:
    # яблуко
    name = 'Apple'
    def __init__(self, x, y, r=20):
        self.x = x
        self.y = y
        self.r = r
    
    def draw(self):
        #image(pictures[1], self.x, self.y, 40, 40)
        stroke(0, 0, 0)
        fill(255, 0, 0)
        circle(self.x, self.y, self.r)    
        line(self.x, self.y - self.r // 10, self.x, self.y - self.r * 3 // 4)
        fill(0, 255, 0)
        ellipse(self.x + self.r // 3, self.y - self.r * 3 // 4, 15, 5)


class Snake:
    # змійка
    name = 'Snake'
    tail = []
    time_last_eat = 0
    cnt = 0
    die = False
    
    def __init__(self, head_x, head_y, r):
        self.head_x = head_x
        self.head_y = head_y
        self.r = r
        self.speed = 2.5
        self.direct_x = 0
        self.direct_y = 0
    
    def move(self):
        self.head_x += self.direct_x * self.speed
        self.head_y += self.direct_y * self.speed
        
        if self.head_x > 400:
            self.head_x -= 400
        if self.head_y > 400:
            self.head_y -= 400
        if self.head_x < 0:
            self.head_x += 400
        if self.head_y < 0:
            self.head_y += 400
            
        self.cnt += 1
        if self.cnt % 5 == 4:
            new_part = (self.head_x, self.head_y)
            if len(self.tail) > 0:
                self.tail.pop()
            self.tail.insert(0, new_part)

    def change_direct(self, new_x, new_y):
        self.direct_x = new_x
        self.direct_y = new_y
        
    def update(self):
        self.move()
        
    def draw_tail(self):
        n = len(self.tail)
        k = n
        for x, y in self.tail:
            if k == 1:
                fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                fill(32, int(float(78*k/n) + 100), 170)
                if k!=n and self.time_last_eat == 0 and Geometry.distance(x, y, self.head_x, self.head_y) < self.r // 7:
                    self.die = True
                
            stroke(0, 0, 0)
            circle(x, y, int(float(15*k/n) + 20))
            
            k -= 1
    
    def draw(self):
        head_color = (32, 178, 170)
        self.update()
        self.draw_tail()
        
        if self.time_last_eat > 0:
            self.time_last_eat -= 1
            if self.time_last_eat < 0:
                self.time_last_eat = 0
            new_snake = Snake(self.head_x, self.head_y, 50)
            new_snake.draw()
            return
        
        if self.direct_y > 0:
            #head
            stroke(0, 0, 0)
            fill(*head_color)
            circle(self.head_x, self.head_y, self.r)
            
            #eyes
            fill(255, 255, 255)
            circle(self.head_x - self.r // 3, self.head_y + self.r // 4, self.r // 3)
            circle(self.head_x + self.r // 3, self.head_y + self.r // 4, self.r // 3)
            
            stroke(253, 245, 230)
            fill(0, 0, 0)
            circle(self.head_x - self.r // 3, self.head_y + self.r // 3.5, self.r // 4.5)
            circle(self.head_x + self.r // 3, self.head_y + self.r // 3.5, self.r // 4.5)
        elif self.direct_y < 0:
            #head
            stroke(0, 0, 0)
            fill(*head_color)
            circle(self.head_x, self.head_y, self.r)
            
            #eyes
            fill(255, 255, 255)
            circle(self.head_x - self.r // 3, self.head_y - self.r // 4, self.r // 3)
            circle(self.head_x + self.r // 3, self.head_y - self.r // 4, self.r // 3)
            
            stroke(253, 245, 230)
            fill(0, 0, 0)
            circle(self.head_x - self.r // 3, self.head_y - self.r // 3.5, self.r // 4.5)
            circle(self.head_x + self.r // 3, self.head_y - self.r // 3.5, self.r // 4.5)
        elif self.direct_x > 0:
            #head
            stroke(0, 0, 0)
            fill(*head_color)
            circle(self.head_x, self.head_y, self.r)
            
            #eyes
            fill(255, 255, 255)
            circle(self.head_x + self.r // 4, self.head_y - self.r // 3, self.r // 3)
            circle(self.head_x + self.r // 4, self.head_y + self.r // 3, self.r // 3)
            
            stroke(253, 245, 230)
            fill(0, 0, 0)
            circle(self.head_x + self.r // 3.5, self.head_y - self.r // 3, self.r // 4.5)
            circle(self.head_x + self.r // 3.5, self.head_y + self.r // 3, self.r // 4.5)
        elif self.direct_x < 0:
            #head
            stroke(0, 0, 0)
            fill(*head_color)
            circle(self.head_x, self.head_y, self.r)
            
            #eyes
            fill(255, 255, 255)
            circle(self.head_x - self.r // 4, self.head_y - self.r // 3, self.r // 3)
            circle(self.head_x - self.r // 4, self.head_y + self.r // 3, self.r // 3)
            
            stroke(253, 245, 230)
            fill(0, 0, 0)
            circle(self.head_x - self.r // 3.5, self.head_y - self.r // 3, self.r // 4.5)
            circle(self.head_x - self.r // 3.5, self.head_y + self.r // 3, self.r // 4.5)
        else:
            #head
            stroke(0, 0, 0)
            fill(0, 255, 255)
            circle(self.head_x, self.head_y, self.r)
            
            #mouth
            stroke(255, 0, 0)
            line(self.head_x - self.r // 5, self.head_y + self.r // 3, self.head_x + self.r // 5, self.head_y + self.r // 3)
            fill(255, 0, 0)
            ellipse(self.head_x, self.head_y + self.r // 3, 20, 10)
            
            #eyes
            stroke(255, 255, 255)
            fill(255, 255, 255)
            circle(self.head_x - self.r // 3, self.head_y, self.r // 3)
            circle(self.head_x + self.r // 3, self.head_y, self.r // 3)
            
            stroke(253, 245, 230)
            fill(0, 0, 0)
            circle(self.head_x - self.r // 3, self.head_y, self.r // 4.5)
            circle(self.head_x + self.r // 3, self.head_y, self.r // 4.5)        
    
    def eat_apple(self):
        self.time_last_eat = 10
        if Info.cnt_apples % 3 == 0:
            self.tail.append((self.head_x, self.head_y))
        
        fill(230, 230, 250)
        circle(self.head_x, self.head_y, 50)
        Info.inc()
        Info.life += 5


class Enemy:
    # ворог
    def __init__(self, x, y, r=60):
        self.x = x
        self.y = y
        self.r = r
    
    def draw(self):
        #head
        stroke(0, 0, 0)
        fill(100, 100, 100)
        circle(self.x, self.y, self.r)
        
        #mouth
        stroke(255, 0, 0)
        line(self.x - self.r // 5, self.y + self.r // 3, self.x + self.r // 5, self.y + self.r // 3)
        fill(255, 0, 0)
        ellipse(self.x, self.y + self.r // 3, 20, 10)
        
        #eyes
        stroke(255, 255, 255)
        fill(255, 255, 255)
        circle(self.x - self.r // 3, self.y, self.r // 3)
        circle(self.x + self.r // 3, self.y, self.r // 3)
        
        stroke(253, 245, 230)
        fill(0, 0, 0)
        circle(self.x - self.r // 3, self.y, self.r // 4.5)
        circle(self.x + self.r // 3, self.y, self.r // 4.5)

    def crash(self):
        for i in range(20):
            stroke(0, 0, 0)
            fill(i * 10, 0, 0)
            circle(self.x, self.y, self.r + i)
    


def finish_game():
    textSize(32)
    fill(0, 0, 0)
    s = "You lose...\nYou got " + str(Info.score) + " scores."
    textSize(40)
    text(s, 40, 180);



objects = []
enemies = []
apples = []
rubbish = []
pictures = []


def setup():
    size(400, 400)

    new_obj1 = Snake(40, 40, 40)
    
    objects.append(new_obj1)
    for i in range(4):
        new_obj2 = Enemy(random.randint(20, 380), random.randint(50, 380), random.randint(35, 50))
        enemies.append(new_obj2)
    new_apple = Apple(random.randint(50, 380), random.randint(50, 380))
    apples.append(new_apple)
    
    back_img = loadImage('img_5.jpg')
    pictures.append(back_img)

def draw():
    image(pictures[0], 0, 0)
        
    
    sz = len(rubbish) + len(apples)
    if Info.cnt_apples == Info.score // 5:
        Info.inc_cnt_apples()
        count = int(Info.sz_apples)
        for i in range(count):
            while True:
                f = False
                new_apple = Apple(random.randint(20, 380), random.randint(50, 380))
                for enemy in enemies:
                    if Geometry.distance(enemy.x, enemy.y, new_apple.x, new_apple.y) < enemy.r // 2 + new_apple.r // 2:
                        f = True
                if not f:
                    apples.append(new_apple)
                    break
            count += 1
    for apple in apples:
        apple.draw()
    for enemy in enemies:
        enemy.draw()
    
    for obj in objects:
        if obj.die == True and obj == objects[-1]:        
            finish_game()
        if not obj.die:
            obj.draw()
        if keyPressed:
            if key == 'w':
                obj.change_direct(0, -1)
            if key == 'a':
                obj.change_direct(-1, 0)
            if key == 'd':
                obj.change_direct(1, 0)
            if key == 's':
                obj.change_direct(0, 1)
            if key == 'e':
                obj.change_direct(0, 0)
            if key == 'q':
                exit()
                    
        for apple in apples:
            if Geometry.distance(apple.x, apple.y, obj.head_x, obj.head_y) < obj.r // 2.5:
                obj.eat_apple()
                apples.remove(apple)
                
        for enemy in enemies:
            if Geometry.distance(obj.head_x, obj.head_y, enemy.x, enemy.y) < obj.r // 2 + enemy.r // 2:
                if Info.life > 0:
                    Info.life -= 1
                if Info.life == 0:
                    obj.die = True
                    enemy.crash()
                    finish_game()
                                                                                                                                                                                                                                                    
    textSize(32)
    fill(0, 0, 0)
    s = "SCORE: " + str(Info.score) + '\n' + "Life: " + str(Info.life)
    textSize(40)
    text(s, 15, 35);
    
