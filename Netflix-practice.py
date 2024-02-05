import random
import time

class content:
    
    def __init__ (self, title, genre, year, duration,category):
        
        self.title = title
        self.genre = genre
        self.year = int(year)
        self.duration = duration
        self.category = category
        
    def get_info(self):
        
        return f"{self.title} is a {self.category} from {self.genre} Genre. It was released in {self.year}. It has a total runtime of {self.duration}."
    
    
class Movie(content):
    
    def __init__(self, title, genre, year, duration,category,director):
        super().__init__(title, genre, year, duration,category)
        self.director = director
        
    def get_info(self):
        
        return f"{super().get_info()} Directed by {self.director}"
    
    
class Tvshow(content):
    
    def __init__(self,title, genre, year, duration,category,seasons):
        super().__init__(title, genre, year, duration,category)
        self.seasons = seasons
    
    def get_info(self):
        
        return f"{super().getinfo()} This TV Series has {self.seasons}" # Method over-riding
    
    
class User:
    SUBSCRIPTION_LEVELS = ['Platinum', 'Gold', 'Silver']
    
    def __init__(self,username,email,subscription_type,platform):
        self._username = username
        self.email = email
        self.subscription_type = subscription_type
        self.platform = platform
        self.watched_movies = []
        self.watched_tv_shows=[]
        
        
        
    def subscribe(self, subscription_type):
        
        
        for id,sub in enumerate(SUBSCRIPTION_LEVELS,1):
            print(f'{id} : {sub}')
            
        selection = int(input('Which level of Subcription you want to subscribe to ? Press that number '))
        if selection == 1:
            self.subscription_type = 'Platinum'
            print('You have subscribed to Platinum level.')
        elif selection == 2:
            self.subscription_type = 'Gold'
            print('You have subscribed to Gold level.')
        elif selection == 3:
            self.subscription_type = 'Silver'
            print('You have subscribed to Silver level.')
        else :
            print('Invalid input')
            self.subscribe()
            
    
    def change_subscription(self):
        
        current_subscription = self.subscription_type
        
        if current_subscription == 'Gold':
            print('Your current subscription is Gold.')
            print('You have the following options:')
            print('1. Stay with Gold')
            print('2. Switch to Platinum')
            print('3. Switch to Silver')
            
            ans = int(input('Enter the number you want to go with ?'))
            if ans == 2:
                print('You have opted for Platinum. Congratulations!')
                self.subscription_type = 'Platinum'
            elif ans == 3:
                print('You have opted to downgrade it to Silver.')
                self.subscription_type = 'Silver'
            else:
                print('You have opted not to change your subscription.')
                
        elif current_subscription == 'Silver':
            print('Your current subscription is Silver.')
            print('You have the following options:')
            print('1. Stay with Silver')
            print('2. Upgrade to Gold')
            print('3. Upgrade to Platinum')
        
            ans = int(input('Enter the number you want to go with ?'))
            if ans == 2:
                print('You have opted to upgrade to Gold.')
                self.subscription_type = 'Gold'
            elif ans == 3:
                print('You have opted to upgrade to Platinum. Congratulations!')
                self.subscription_type = 'Platinum'
            else:
                print('You have opted not to change your subscription.')
                
        elif current_subscription == 'Platinum':
            print('Your current subscription is Platinum.')
            print('You have the following options:')
            print('1. Stay with Platinum')
            print('2. Downgrade to Gold')
            print('3. Downgrade to Silver')
        
            ans = int(input('Enter the number you want to go with ?'))
            if ans == 2:
                print('You have opted to downgrade to Gold.')
                self.subscription_type = 'Gold'
            elif ans == 3:
                print('You have opted to downgrade to Silver.')
                self.subscription_type = 'Silver'
            else:
                print('You have opted not to change your subscription.')
            
        else:
            print('Invalid subscription type.')
            
                
    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self,new_username):
        self._username = new_username
    
    
    def update_profile(self) :
        attempts = 3
        while attempts>0:
            
            new_username = input('Enter new username:(type "exit" to cancel) ')
            
            if new_username.lower() == 'exit':
                print('Profile update cancelled.')
                break
            
            
            elif new_username not in self.platform.users.keys() and new_username != self._username :
                self._username = new_username
                print('Username has been successfully changed !')
                break
            else:
                print('You cannot use this username. This has already been taken.')
                attempts -= 1 
        else:
            print('Maximum attempts reached. Please try again later.')
        
    def display_watch_history(self):
        print(f"Watch History for {self._username}:")
        print("Watched Movies:")
        for movie in self.watched_movies:
            print(movie.title)
            
        print("\nWatched TV Shows:")
        for tv_show in self.watched_tv_shows:
            print(tv_show.title)
            
        
        
class StreamingPlatform :
    
    def __init__(self):
        
        self.movies_list = []  
        self.tv_shows_list = []  
        self.users = {}
        self.default_subscription = 'Free'
        
    
    def add_user(self,username,email,subscription_type=None):
        
        if subscription_type is None or subscription_type == '':
            subscription_type = self.default_subscription
        
        new_user = User(username,email,subscription_type,self)   #(CHECK)composition or agrregation as User class is used in streaming class
        self.users[username] = new_user
        
        # Fetch the updated subscription type from the User class
        updated_subscription_type = new_user.subscription_type
        print(f"Welcome, {username}! Your subscription type is {updated_subscription_type}.")
        
        if updated_subscription_type == 'Free':
            print("Consider upgrading to enjoy more content!")
        elif updated_subscription_type == 'Platinum':
            print("You have access to all premium content. Enjoy!")
        else:
            print("You have access to basic content. Upgrade for more features.")
        
       
    def get_user(self,username):
        
        if username in self.users:
            
            user_obj = self.users[username]
                
            print(f"Username is : {user_obj.username}")
            print(f"Email id is : {user_obj.email}")
            print(f"Subscription type is : {user_obj.subscription_type}")
            
        else:
            print('User not found.')
            
            
    
    def add_new_movie(self,title, genre, year, duration,category,director):
        
        new_movie = Movie(title, genre, year, duration,category,director)
        self.movies_list.append(new_movie)
        
    
    def add_new_tvshow(self,title, genre, year, duration,category,seasons):
        
        new_tvshow = Tvshow(title, genre, year, duration,category,seasons)
        self.tv_shows_list.append(new_tvshow)


    def get_movie_titles(self):
        
        return [movie.title for movie in self.movies_list]

    def get_tv_show_titles(self):
        
        return [tvshow.title for tvshow in self.tv_shows_list]
        
        
        
    def what_to_watch(self):
        
        print('What do you want to watch ?')
        a = int(input("If you want to watch Movies Enter 1.If you want to watch Tvhows Enter 2 :-"))
        
        if a==1:
            print('code entered this block')
            for id,movie in enumerate(self.movies_list,1):
                print('Entered 2')
                title, genre, year, duration,category,director = movie
                movie_info = Movie(title, genre, year, duration, category).get_info()
                print(f"{id},{title} ---- {movie_info}")
            a=0
            while a<3:
                choice = int(input('Enter the number of movie you want to watch: '))
            
                if 1 <= choice <= len(self.movies_list):
                    selected_movie = self.movies_list[choice - 1]
                    self.display_advertisement()
                    print(f"Now playing... {selected_movie[0]}")
                    self.users[username].watched_movies.append(selected_movie)
                    break
                
                else :
                    print('"Invalid input. Please enter a valid number."')
                    a=a+1
                    
            else:
                print("Maximum attempts reached. Please try again later.")
               
                
        elif a==2:
            
            
            for id,tvshow in enumerate(self.tv_shows_list,1):
                title, genre, year, duration,category,seasons = tvshow
                tvshow_info = Tvshow(title, genre, year, duration,category,seasons).get_info()
                print(f"{id},{title} ---- {tvshow_info}")
            a=0
            while a<3:
                choice = int(input('Enter the number of tvshow you want to watch: '))
            
                if 1 <= choice <= len(self.tv_shows_list) :
                    selected_tvshow = self.tv_shows_list[choice - 1]
                    self.display_advertisement()
                    print(f"Now playing... {selected_tvshow[0]}")
                    self.users[username].watched_tv_shows.append(selected_tvshow)
                    break
                
                else :
                    print('"Invalid input. Please enter a valid number."')
                    a=a+1
                    
            else:
                print("Maximum attempts reached. Please try again later.")
                
                
        else:
            print('Invalid input')
            
    
class Advertisement:
    
    ads_dict = {}
    
    def __init__(self,ad_id,ad_content,target_audience):
        
        self.ad_id = ad_id
        self.ad_content = ad_content
        self.target_audience = target_audience
        self.add_to_ads_dict()
        
    @classmethod
    def display_advertisement(cls):
        ad_ids = list(cls.ads_dict.keys())
        if ad_ids:
            random_ad_id = random.choice(ad_ids)
            selected_ad = cls.ads_dict[random_ad_id]
            print(f"Advertisement ID: {random_ad_id}")
            print(f"Content: {selected_ad['Content']}")
            print(f"Target Audience: {selected_ad['Target Audience']}")
            print("Playing advertisement...")
            time.sleep(10)
    
    @classmethod    
    def display_ad_details(cls):
        
        print("Ads stored in the dictionary:")
        for ad_id, ad_info in cls.ads_dict.items():
            print(f"Ad ID: {ad_id}")
            print(f"Content: {ad_info['Content']}")
            print(f"Target Audience: {ad_info['Target Audience']}")
            print()

        
    def add_to_ads_dict(self):
        
        Advertisement.ads_dict[self.ad_id] = {
            "Content": self.ad_content,
            "Target Audience": self.target_audience
        }     


class DiscussionBoard:
    def __init__(self):
        self.movie_discussions = {}
        self.tv_show_discussions = {}

    def start_movie_discussion(self, movie_title, initial_post):
        
        self.movie_discussions[movie_title] = [initial_post]

    def start_tv_show_discussion(self, tv_show_title, initial_post):
        
        self.tv_show_discussions[tv_show_title] = [initial_post]

    def add_movie_post(self, movie_title, post_content):
        
        if movie_title in self.movie_discussions:
            self.movie_discussions[movie_title].append(post_content)
        else:
            print("Discussion for this movie not found.")

    def add_tv_show_post(self, tv_show_title, post_content):
        
        if tv_show_title in self.tv_show_discussions:
            self.tv_show_discussions[tv_show_title].append(post_content)
        else:
            print("Discussion for this TV show not found.")

    def get_movie_discussion(self, movie_title):
        
        if movie_title in self.movie_discussions:
            return self.movie_discussions[movie_title]
        else:
            return None

    def get_tv_show_discussion(self, tv_show_title):
        
        if tv_show_title in self.tv_show_discussions:
            return self.tv_show_discussions[tv_show_title]
        else:
            return None
        
class Watchlist:
    def __init__(self, streaming_platform):
        self.streaming_platform = streaming_platform
        self.watchlist_items = []

    def display_movies(self):
        
        movies_list = self.streaming_platform.movies_list
        print("Movies available:")
        for index, movie in enumerate(movies_list, 1):
            print(f"{index}. {movie.title}")

    def display_tv_shows(self):
        
        tv_shows_list = self.streaming_platform.tv_shows_list
        print("TV Shows available:")
        for index, tv_show in enumerate(tv_shows_list, 1):
            print(f"{index}. {tv_show.title}")

    def add_to_watchlist(self, selection_type, selected_item_number):
        if selection_type == 'movie':
            movies_list = self.streaming_platform.movies_list
            if 1 <= selected_item_number <= len(movies_list):
                selected_movie = movies_list[selected_item_number - 1]
                self.watchlist_items.append(selected_movie)
                print(f"{selected_movie.title} added to your watchlist.")
            else:
                print("Invalid movie selection.")

        elif selection_type == 'tv_show':
            tv_shows_list = self.streaming_platform.tv_shows_list
            if 1 <= selected_item_number <= len(tv_shows_list):
                selected_tv_show = tv_shows_list[selected_item_number - 1]
                self.watchlist_items.append(selected_tv_show)
                print(f"{selected_tv_show.title} added to your watchlist.")
            else:
                print("Invalid TV show selection.")
        else:
            print("Invalid selection type.")