def trim_text(text, max_length=5000):
    # Remove undecodable characters by encoding to bytes and decoding back
    try:
        cleaned_text = text.encode('utf-8', errors='ignore').decode('utf-8')
    except UnicodeDecodeError:
        cleaned_text = text

    # Initialize variables
    current_length = 0
    trimmed_words = []

    # Generator to yield words from the cleaned text
    def word_generator(text):
        for word in text.split():
            yield word

    # Process words with a generator
    for word in word_generator(cleaned_text):
        word_length = len(word)
        if current_length + word_length + (1 if trimmed_words else 0) > max_length:
            break
        trimmed_words.append(word)
        current_length += word_length + (1 if trimmed_words else 0)
    
    # Join the words into a single string and return
    return ' '.join(trimmed_words)

# Example usage
text = """When Your Wi-Fi Goes Down and the Apocalypse Hits: Hilarious Reactions You Can't Miss!"
Struggling with a Wi-Fi outage? This meme video captures the ultimate facepalm moments and over-the-top reactions from people who just can't handle a day without their precious internet. From the overdramatic breakdowns to the most relatable expressions of frustration, this reel has it all. Dive into a world of #InternetFails, #WiFiProblems, and #RelatableMoments. Whether you're dealing with a slow connection or just love watching people overreact, this video is perfect for a laugh. Share with friends who always complain about their Wi-Fi speed and need a good chuckle!
"Pet Owners vs. The Vacuum Cleaner: The Ultimate Showdown!"
Ever wondered how your pets react to the vacuum cleaner? This meme video showcases the most hilarious and unexpected pet reactions when their nemesis, the vacuum, makes an appearance. From the epic hide-and-seek strategies to the most fearless confrontations, this reel is packed with #PetFails, #VacuumVsPets, and #FurryFriends. Perfect for a laugh after a long day or to share with fellow pet lovers who’ll appreciate the struggle of keeping pets and vacuums at peace!
"Monday Mornings: The Struggle Is Real – Watch the Best Workday Woes!"
Monday mornings got you feeling down? This meme video captures the struggle of transitioning from weekend relaxation to workday grind with side-splitting humor. Featuring epic MondayBlues moments, office fails, and the universal feeling of dreading the workweek, this reel is filled with #MondayMotivation and #OfficeHumor. Whether you’re working from home or heading into the office, this video will have you nodding in agreement and laughing out loud!
"When You Try to Be Healthy but Pizza Calls Your Name: The Struggle Is Real!"
Ever tried to stick to a diet but your favorite pizza keeps calling your name? This meme video captures the funniest diet struggles and pizza cravings with hilarious skits and relatable scenarios. Featuring the ultimate #FoodFails, #PizzaLovers, and #HealthyLiving challenges, this reel is perfect for anyone who has ever had a battle with their cravings. Share with friends who can’t resist a cheesy slice of pizza and enjoy a good laugh!
"Zoom Meetings Gone Wrong: The Funniest Virtual Fails You Need to See!"
Struggling with Zoom meetings? This meme video highlights the funniest and most cringe-worthy moments from virtual meetings that went hilariously wrong. From awkward silences to unexpected interruptions, this reel captures the best of #VirtualFails, #ZoomMeetingStruggles, and #WorkFromHomeLife. Perfect for a laugh with colleagues or to share with anyone who’s ever had a Zoom mishap!
"Sibling Rivalry: Hilarious Pranks and Feuds You’ll Totally Relate To!"
Siblings always find a way to prank each other, and this meme video showcases the best of those hilarious feuds and pranks. Featuring epic #SiblingRivalry moments, playful arguments, and the best sibling pranks, this reel is a must-watch for anyone who has ever had a brother or sister. Share with your siblings and enjoy the laughs as you reminisce about your own family shenanigans!
"The Ultimate ‘Trying to Look Cool’ Fails: When Your Swagger Falls Short!"
Think you’re smooth but end up making a hilarious fool of yourself? This meme video captures the funniest moments of people trying to look cool and falling short in the most epic ways. With #FailMoments, #CringeWorthyAttempts, and #SwaggerFails, this reel is perfect for anyone who has ever tried and failed to impress. Share with friends who appreciate a good laugh at the expense of overconfident moves!
"Expectation vs. Reality: The Funniest Discrepancies in Everyday Life!"
Ever had high expectations only to face hilarious realities? This meme video compares expectations vs. reality in the most relatable scenarios, from cooking disasters to workout fails. Featuring #ExpectationVsReality, #LifeFails, and #DailyStruggles, this reel will have you laughing and nodding along. Share with anyone who’s ever faced a disappointing outcome after setting high hopes!
"The Office Prank War: Hilarious and Ingenious Desk Pranks You Have to See!"
Office pranks take center stage in this meme video, showcasing the most creative and funny desk pranks. From sneaky setups to hilarious reactions, this reel is packed with #OfficePranks, #WorkplaceHumor, and #PrankWars. Perfect for sharing with colleagues or anyone who loves a good office prank and enjoys some light-hearted workplace humor!
"Parents Trying to Be Hip: The Funniest Attempts to Keep Up with Trends!Watch as parents hilariously attempt to keep up with the latest trends and fail in the most amusing ways. This meme video features the funniest #ParentFails, #TrendAttempts, and #HipMoments, capturing the essence of generational gaps and the struggle to stay cool. Share with friends who’ll appreciate the humor in watching parents navigate today’s trends and have a good laugh!
Each description is tailored to be witty, engaging, and optimized for high search engine rankings while covering a broad range of meme-related topics.


write robuts  description for mees videos Create a witty and engaging description for a meme video that highlights the funniest moments and makes viewers eager to share. The description should include popular keywords and hashtags related to trending topics or viral content, ensuring it ranks high in search results. Mention any relevant cultural references, social media trends, or popular phrases to make the description relatable and searchable and informative description to achieve top search engine rankings, maximize visibility, and enhance discoverability on YouTube. The keywords must be highly relevant, compelling, and designed to attract a broad audience. Ensure the inclusion of various keyword types, such as long-tail phrases, trending topics, and should be approximately 5000 characters long, but no less than 4500 characters, to provide a comprehensive and detailed exploration of the subject matter. write 10 description 
ChatGPT
"""

trimmed_text = trim_text(text)
print(trimmed_text)
