import time
from time import sleep
import csv
import os
from PIL import Image
import json
from youtubesearchpython import VideosSearch
import requests
time_schedule = 1
website_url = "http://demosite.local/"
website_pass ="iwEy 81A4 ZTjI QBQZ jv0o gnGo"
user_admin = "admin"
status = 'draft'
author = 1

image_path = r'C:\Users\New folder'
keywords_path = r'C:\Users\New folder (2)\keywords.csv'

api_requests_av = 2
openai_in_engines = "text-davinci-003"

temperature= 0.7
top_p = 1
frequency_penalty = 0
presence_penalty=0

from dotenv import load_dotenv
load_dotenv()
pexels_api = os.getenv(PEXELS_API)


def headerss(wp_user, wp_pass):
    """This functions will return (wp headers) for WordPress.
    input: You have to input (username & password)"""
    import base64
    wp_credential = f'{wp_user}:{wp_pass}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
    return wp_header
#------------------------------------
#******** Content Genaret Functions ************

def text_formating(sentences):
    sentences = sentences.replace('.', '.---').split('---')
    retun_text1 = '<!-- wp:paragraph --><p>' + ''.join(sentences[0:5]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    retun_text2 = '<!-- wp:paragraph --><p>' + ''.join(sentences[5:10]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    retun_text3 = '<!-- wp:paragraph --><p>' + ''.join(sentences[10:15]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    retun_text4 = '<!-- wp:paragraph --><p>' + ''.join(sentences[15:20]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    retun_text5 = '<!-- wp:paragraph --><p>' + ''.join(sentences[20:25]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    retun_text6 = '<!-- wp:paragraph --><p>' + ''.join(sentences[25:30]).replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','').strip() + '</p><!-- /wp:paragraph -->'
    return retun_text1.strip() + retun_text2 + retun_text3 + retun_text4 + retun_text5 + retun_text6
def faq_render(sentences):
    sentences = sentences.replace('.', '.---').split('---')
    final_faq = '<!-- wp:heading --><h2>FAQs</h2><!-- /wp:heading -->'+'<!-- wp:paragraph --><p>'+''.join(sentences)\
        .strip().replace('Q1. ','<strong>').strip().replace('A1. ','<br></strong>')\
        .strip().replace('Q2. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A2. ','<br></strong>')\
        .strip().replace('Q3. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A3. ','<br></strong>')\
        .strip().replace('Q4. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A4. ','<br></strong>')\
        .strip().replace('Q5. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A5. ','<br></strong>')\
        .strip().replace('Q6. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A6. ','<br></strong>')\
        .strip().replace('Q7. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A7. ','<br></strong>')\
        .strip().replace('Q8. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A5. ','<br></strong>')\
        .strip().replace('Q9. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A9. ','<br></strong>')\
        .strip().replace('Q10. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A10. ','<br></strong>')\
        .strip().replace('Q11. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A11. ','<br></strong>')\
        .strip().replace('Q12. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A12. ','<br></strong>')\
        .strip().replace('Q13. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A13. ','<br></strong>')\
        .strip().replace('Q14. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A14. ','<br></strong>')\
        .strip().replace('Q15. ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A15. ','<br></strong>')\
        .strip().replace('Q1: ', '<strong>').strip().replace('A1:', '<br></strong>')\
        .strip().replace('Q2: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A2: ', '<br></strong>')\
        .strip().replace('Q3: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A3: ', '<br></strong>')\
        .strip().replace('Q4: ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A4: ', '<br></strong>')\
        .strip().replace('Q5: ','</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A5: ', '<br></strong>')\
        .strip().replace('Q6: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A6: ', '<br></strong>')\
        .strip().replace('Q7: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A7: ', '<br></strong>')\
        .strip().replace('Q8: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A8: ', '<br></strong>')\
        .strip().replace('Q9: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A9: ', '<br></strong>')\
        .strip().replace('Q10: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A10: ', '<br></strong>')\
        .strip().replace('Q11: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A11: ', '<br></strong>')\
        .strip().replace('Q12: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A12: ', '<br></strong>')\
        .strip().replace('Q13: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A13: ', '<br></strong>')\
        .strip().replace('Q14: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A14: ', '<br></strong>')\
        .strip().replace('Q15: ', '</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><strong>').strip().replace('A15: ', '<br></strong>')\
        .strip()+'</p><!-- /wp:paragraph -->'
    return final_faq
def h2(text):
    """
    This function converts from normal text to WordPress Gutenberg h2
    """
    code_h2 = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code_h2
def h3(text):
    """
    This function converts from normal text to WordPress Gutenberg h3
    """
    code_h3 = f'<!-- wp:heading {{"level":3}} --><h3>{text}</h3><!-- /wp:heading -->'
    return code_h3
def openai_render_test(command,delay=api_requests_av):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    time.sleep(delay)
    import openai
    openai.api_key = os.getenv(OPENAI_API)
    openai_engines = openai_in_engines
    response = openai.Completion.create(
        model=openai_engines,
        prompt=command,
        temperature=temperature,
        max_tokens=500,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    openos = response["choices"][0]["text"].strip()
    return openos
def outline_data(text):
    main_data = ''
    data = openai_render_test(f'Write a killer blog 3 outline for the following request from a customer.\n REQUEST: "{text}"\nBrainstorm a DATA format of sections for this blog post. The outline should meet the customer\'s request and each section should be highly descriptive.\nDATA Example : [\n  {{"h1": "Title "}}, \n  {{"h2": "Heading Two"}},\n  {{"h3": "Heading Three"}},\n  {{"h3": "Heading Three"}},\n  {{"h2": "Heading Two"}},\n  {{"h3": "Heading Three"}},\n  {{"h3": "Heading Three"}},\n  {{"h3": "Heading Three"}},\n  {{"h2": "Heading Two"}},\n  {{"h3": "Heading Three"}},\n  {{"h3": "Heading Three"}},\n  {{"h2": "Heading Two"}}\n]\n\n\nSECTIONS:\n[')
    main_data += '['+str(data)
    return main_data
#******** Content Genaret Functions End ************
#******** Image ID Functions Start ************
def wp_image_id(website_url,website_pass,user_admin,save_image_keyword,paxbay_img_url):
    import os
    from httpx import get, post
    import base64
    file_path_ss = image_path
    normalized_file_path = os.path.normpath(file_path_ss)
    def image_from_media(img_src):
        files = {'file': open(img_src, 'rb')}
        return files
    def headers(wp_user, wp_pass):
        wp_credential = f'{wp_user}:{wp_pass}'
        wp_token = base64.b64encode(wp_credential.encode())
        wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
        return wp_header

    res = get(f'{paxbay_img_url}')
    with open(f'{normalized_file_path}\\{save_image_keyword}.jpg', 'wb') as file:
        file.write(res.content)
        features_img = image_from_media(f'{normalized_file_path}\\{save_image_keyword}.jpg')
    image = Image.open(f'{normalized_file_path}\\{save_image_keyword}.jpg')
    image = image.resize((640, 360))
    image.save(f'{normalized_file_path}\\{save_image_keyword}.jpg')
    header = headers(user_admin, website_pass)
    media_upload_json = f'{website_url}wp-json/wp/v2/media' # change the website address
    res_id = requests.post(media_upload_json, files=features_img, headers=header, verify=False)
    feature_img_id = res_id.json()
    return feature_img_id
def pexels(query):
    response = requests.get(f'https://api.pexels.com/v1/search?query={query}&per_page={5}', headers={'Authorization': pexels_api}).json()
    return response
#******** Image ID Functions End ************
def ytvideo(text):
    videosSearch = VideosSearch(text, limit = 2)
    video_link = videosSearch.result().get("result")[0].get('id')
    wp_lik_youtube = f'<iframe width="550" height="320" src="https://www.youtube.com/embed/{video_link}"></iframe>'
    return wp_lik_youtube
with open(keywords_path) as file:
  reader = csv.DictReader(file)
  for row in reader:
    line =(row['keyword'])
    categories = row['id']
    try:
        line = line.strip()
        image_url_one = pexels(line).get("photos")[0].get("src").get('original')
        image_url_two = pexels(line).get("photos")[1].get("src").get('original')
        image_title_two = pexels(line).get("photos")[1].get('alt')
        if not image_title_two:
            image_title_two = line+" featured image"
        featured_img_id = wp_image_id(website_url=website_url, website_pass=website_pass,
                                      user_admin=user_admin, save_image_keyword=image_title_two,
                                      paxbay_img_url=image_url_one).get('id')
        content_image = wp_image_id(website_url=website_url, website_pass=website_pass, user_admin=user_admin,
                                    save_image_keyword=line,
                                    paxbay_img_url=image_url_two).get('guid').get('rendered')
        image_code = f'<!-- wp:image {{"sizeSlug":"large"}} --><figure class="wp-block-image size-large"><img src="{content_image}" alt="{line}"/></figure><!-- /wp:image -->'

        try:
            data = openai_render_test(f'Write a killer blog outlines for the following request from a customer. The Outlines must always be below 60 characters.\n\nREQUEST: \"{line}"\n\nBrainstorm Must be a Use DATA Example format of sections for this blog post. The outlines should meet the customer\\n s request and each section should be highly descriptive.\nDATA Example : [\n  {{\"h1\": \"Title \"}}, \n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}}\n]\n\n\nSECTIONS:\n[')
            main_data = '[' +data
            main_datas = json.loads(main_data, strict=False )
            # print('one',main_datas)
        except:
            data = openai_render_test(f'Write a killer blog outlines for the following request from a customer. The Outlines must always be below 60 characters.\n\nREQUEST: \"{line}"\n\nBrainstorm Must be a Use DATA Example format of sections for this blog post. The outlines should meet the customer\\n s request and each section should be highly descriptive.\nDATA Example : [\n  {{\"h1\": \"Title \"}}, \n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h3\": \"Heading Three\"}},\n  {{\"h2\": \"Heading Two\"}}\n]\n\n\nSECTIONS:\n[')
            main_data = '[' +data
            main_datas = json.loads(main_data, strict=False)
            # print('two',main_datas)
        for d in main_datas:
            if "Title" in d:
                d["h1"] = d.pop("Title")
            if "Heading Two" in d:
                d["h2"] = d.pop("Heading Two")
            if "Heading Three" in d:
                d["h3"] = d.pop("Heading Three")
        for element in main_datas:
            for key in list(element.keys()):
                if key == 'h2' and 'Conclusion' in element[key]:
                    element['con'] = element.pop('h2')
        has_con = False
        for d in main_datas:
            if 'con' in d:
                has_con = True
                break
        if not has_con:
            main_datas.append({'con': "Conclusion"})
        # print('final',main_datas)
        output = ""
        title = ""
        i = 0
        for item in main_datas:
            if "h1" in item:
                title = (item["h1"].strip())
                intro = openai_render_test(f'Write a High Quality SEO Friendly killer Blog Intro for an {title}')
                wp_intro = (text_formating(intro)).strip()
                output += "\n" + wp_intro + "\n".strip()
            if "h2" in item:
                heding_two = (f"  {item['h2']}".strip())
                wp_h2 = h2(heding_two)
                paragraph_h2 = openai_render_test(f'"\"\"\"\nBlog Section Title: {heding_two}, Main Keyword: {line}\n\"\"\"\nWrite this blog section in more than 150 words in detail with professional para in, a witty and clever explanation:"')
                wp_h2_pragraph = (text_formating(paragraph_h2).strip())
                output += wp_h2 + "\n" + wp_h2_pragraph + "\n".strip()
            if "h3" in item:
                heding_three = (f"    {item['h3']}".strip())
                wp_h3 = h3(heding_three)
                paragraph_h3 = openai_render_test(f'"\"\"\"\nBlog Section Title: {heding_three}, Main Keyword: {line}\n\"\"\"\nWrite this blog section into a details professional para, witty and clever explanation:"')
                wp_h3_pragraph = (text_formating(paragraph_h3).strip())
                output += wp_h3 + "\n" + wp_h3_pragraph + "\n".strip()
            if "con" in item:
                conclution_hed_2 = (f"    {item['con']}".strip())
                wp_con = h2(conclution_hed_2)
                paragraph_con = openai_render_test(f'"Write a conclusion, witty and clever explanation in \" {line}\" :\n"')
                wp_h2_pragraph_con = (text_formating(paragraph_con).strip())
                output += wp_con + "\n" + wp_h2_pragraph_con + "\n".strip()
            if i == 2:
                output += image_code
            i += 1
        faq_main = openai_render_test( f'"Example:\nQ1. Santance..................\nA1. Santance..................\nQ2. Santance..................\nA2. Santance..................\nQ3. Santance..................\nA3. Santance..................\n......................\n..........................\n............................................\nKeyword: {line}\n\nBrainstorm Write Must Be 4 to 6  Defarent type faqs With an Answer in This Keyword\nMust Be Following This Example Format:\n",')
        final_faq = faq_render(faq_main)
        output += final_faq
        main_video = ytvideo(line)
        output += main_video
        keyss = output.split("<!-- wp:paragraph --><p></p><!-- /wp:paragraph -->")
        filtered_lines = [line for line in keyss if line.strip()]
        filtered_content = "\n".join(filtered_lines)  # ******
        main_title = openai_render_test(f'Write a cut high-level search engine and SEO friendly a Blog Title for "{line}"')
        titless = (main_title.replace('"', ''))  # *****
        main_data_content = {'title': titless,
                             'slug': line,
                             'status': status,
                             'content': filtered_content,
                             'categories': categories,
                             'author': author,
                             'format': 'standard',
                             'featured_media': featured_img_id,
                             }
        url_wp_access = website_url + '/wp-json/wp/v2'
        headers = headerss(wp_user=user_admin, wp_pass=website_pass)
        r = requests.post(url_wp_access + '/posts', headers=headers, json=main_data_content).json().get('guid').get('rendered')
        print(line+" "+r+' Has Been Posted')
    except IndexError:
        print(f'Post Failed Try Again: {line}')
        pass
    sleep(time_schedule)




















