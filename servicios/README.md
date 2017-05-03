# Servicios
En esta carpeta se definen los servicios utilizados para el Sistema de 
Procesamiento de Comentarios (SPC). Las especificaciones de todos los 
servicios se realizaron utilizando el blueprint de Apiary. Los servicios y 
sus especificaciones aparecen a continuación.


## Procesador de Comentarios de IMDb
  
FORMAT: 1A  
HOST: http://localhost:8085

## Information Service [/api/tweet/analizar{?titulo}]

+ Parameters
    + titulo - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Ejecutar el sistema.
2. Ingresar a la dirección: 
http://localhost:8085/api/movie/information?titulo=pretty little liars

---

## Gestor de comentarios de Twitter
  
FORMAT: 1A  
HOST: http://localhost:8085

## Tweet Manager Service [/api/tweet/search{?titulo}]

+ Parameters
    + titulo - Corresponde al título de la película o serie de Netflix.

### Get Tweets [GET]

+ Response 200 (application/json)

        [
            {
                "user_name": "vimadmusic",
                "tweet_hashtag": "#Narcos",
                "tweet_body": "@ViMad Así mismo... deberían ver #Narcos en @netflix para que se les rompa el sello de inocencia que tienen en sus ojos.",
                "tweet_date": "Tue May 02 20:17:45 +0000 2017"
            },
            {
                "user_name": "jlC3EJLLmEEIXre",
                "tweet_hashtag": "#Narcos",
                "tweet_body": "RT @netflix: Agent Peña, Agent Murphy, off duty. #Narcos #GoldenGlobes https://t.co/oBTHf1ByVA",
                "tweet_date": "Mon May 01 07:31:24 +0000 2017"
            },
            {
                "user_name": "AlexHaddo",
                "tweet_hashtag": "#Narcos",
                "tweet_body": "RT @netflix: You didn't think the story died with Pablo, did you? #Narcos Season 3, 2017. https://t.co/BxY3Pgrgzw",
                "tweet_date": "Sun Apr 30 23:50:41 +0000 2017"
            }
        ]

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Ejecutar el sistema.
2. Ingresar a la dirección: 
http://localhost:8085/api/tweet/search?titulo=Narcos