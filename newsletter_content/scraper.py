import datetime
from datetime import date
import locale
# Web Scrapping
import requests
from bs4 import BeautifulSoup
# Send Email
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today = date.today()

devociónes = {
    "enero":
        "El mes de enero está dedicado al Niño Jesús y, en particular, al Santísimo Nombre de Jesús. Ocho días después de Navidad se honra la devoción del Santísimo Nombre de Jesús, para celebrar el día en que San José lo circuncidió y le dio el nombre. Este culto devocional se ha celebrado desde los orígenes de la Iglesia. De hecho, parece que ya los santos Pedro y Pablo contribuyeron a su difusión, y más tarde, en la época medieval, San Francisco de Asís fue un propugnador. San Bernardino y sus cofrades lo convirtieron en una fiesta litúrgica. La devoción del Santísimo Nombre de Jesús se centra en el poder del nombre de Jesús, defensa y ornamentación para los fieles, protección contra el mal y valioso talismán contra demonios, enfermedades y debilidades.",
    "febrero":
        "El mes de febrero está dedicado al Espíritu Santo, la tercera persona de la Santísima Trinidad. El Espíritu Santo es Dios y, al mismo tiempo, el don de amor que Dios le da a sus devotos hijos. Desciende sobre los creyentes como una llama ardiente y hace sus palabras aladas, para que puedan alcanzar al Padre. Febrero dedica sus devociones también a la Sagrada Familia, la familia por excelencia, la familia compuesta por Jesús, José y María. Las oraciones y letanías están dedicadas a este ejemplo perfecto de Amor y Fe, al que todos deberían aspirar para vivir en serenidad y plenitud. Las devociones a la Sagrada Familia expresan la voluntad de hacer lo que agrada a Jesús, María y José y evitar lo que puede desagradarles.",
    "marzo":
        "Marzo es el mes de la devoción a san José, porque su fiesta mayor es el día 19 de marzo: san José, el esposo de la Virgen; el hombre justo que tuvo la honra y la gloria de ser escogido por Dios para se el padre adoptivo de su hijo hecho hombre.\nLe tocó a José darle el nombre de Jesús. En este mes la Iglesia nos invita a mirar este modelo de padre amoroso, esposo fiel y casto, trabajador dedicado, listo a hacer, sin demora la voluntad de Dios. La Iglesia le rinde culto de “protodulia” (primera veneración).\nExisten muchas oraciones dedicadas a san José, la letanía en su honor, el rosario de san José, etc..\n\nSanta Teresa de Ávila dijo que siempre que le pedía algo a san José, en una de sus fiestas (19 de marzo o 1 de mayo), nunca dejó de ser escuchada. Todos sus Carmelos reformados tuvieron el nombre de san José.",
    "abril":
        "Abril está dedicado a la Eucaristía y al Divino Espíritu Santo. Casi siempre el día de Pascua cae en abril; e incluso cuando cae en marzo, el periodo pascual de 40 días continúa en abril.\n\n\La Eucaristía es el centro de la vida de la Iglesia. Ella es el sacrificio de Cristo que se actualiza (se vuelve presente) en el altar, en la celebración de la misa; y alimento (banquete) del cordero que se da como alimento espiritual.\n\n\Es la mayor prueba de amor de Jesús con nosotros. Además de la misa, Él permanece en estado de víctima ofrecida permanentemente al Padre en nuestros sagrarios, para ayudarnos en todas las necesidades y estar siempre con nosotros.\n\n\'Habiendo amado a los suyos que estaban en el mundo, los amó hasta el extremo\' (Jn 13,1).",
    "mayo":
        "Mayo es el mes de la Virgen María porque está lleno de sus fiestas: 13 de mayo (Nuestra Señora de Fátima), la Visitación (31 de mayo).\n\nY por ser la Madre de Dios y nuestra, el mundo cristiano conmemora el día de las madres el segundo domingo de mayo, (en algunos países el primero, en otros día 10) rogándole que defienda, proteja y auxilie a todas las madres en su difícil misión.\n\nLa devoción a la Virgen María quiere destacar el papel fundamental de ella de mediadora de todas las gracias, intercesora permanente del pueblo de Dios, modelo para las madres cristianas, pura y santa, siempre lista y dispuesta a hacer la voluntad de Dios.\n\nEs el mes por excelencia para que las novias se casen y se consagren en sus bodas a Ella, es el mes de rezar el Rosario y su bella letanía lauretana.",
    "junio":
        "Junio es el mes del Sagrado Corazón de Jesús. Una devoción que comenzó alrededor del año 1620 cuando Jesús se la pidió a santa Margarita María Alacoque.\n\nFue extendida en el mundo por san Claudio de La Colombiere, que era director espiritual de la santa.\n\nEra un tiempo en que había una peligrosa herejía llamada jansenismo, que impedía a los católicos comulgar con frecuencia e inculcaba miedo de Dios a la personas.\n\nLa devoción al Sagrado Corazón muestra a un Jesús humano, misericordioso, listo a perdonar como el Padre al hijo pródigo; y que anima a la participación de la adoración a la Eucaristía y a recibir la comunión el primer viernes de cada mes.\n\nConocemos la bella letanía del Sagrado Corazón de Jesús e innumerables oraciones compuestas por los santos.",
    "julio":
        "El mes de Julio está dedicado a la Preciosa Sangre de Nuestro Señor; y la fiesta específica es el primer domingo del mes.\n\nLa Sangre de Jesús es el \'precio de nuestra salvación\'.\n\nLa piedad cristiana siempre manifestó, a través de los siglos, especial devoción a la Sangre de Cristo derramado para la remisión de los pecados de todo el género humano, y atravesando la historia hasta el día de hoy con su presencia real en el sacramento de la Eucaristía.\n\nEl papa Juan Pablo II, en su carta apostólica Angelus Domini, subrayó la invitación de Juan XXIII sobre el valor infinito de esa Sangre, de la cual \'un sola gota puede salvar al mundo entero de cualquier culpa.\'",
    "agosto":
        "Agosto es el mes dedicado a el Inmaculado Corazón de María. Ésta fiesta está íntimamente vinculada con la del Sagrado Corazón de Jesús, la cual se celebra el día anterior, viernes. Ambas fiestas se celebran, viernes y sábado respectivamente, en la semana siguiente al domingo de Corpus Christi. Los Corazones de Jesús y de María están maravillosamente unidos en el tiempo y la eternidad desde el momento de la Encarnación. La Iglesia nos enseña que el modo más seguro de llegar a Jesús es por medio de María. Por eso nos consagramos al Corazón de Jesús por medio del Corazón de María.\n\nLa fiesta del Corazón Inmaculado de María fue oficialmente establecida en toda la Iglesia por el papa Pío XII, el 4 de mayo de 1944, para obtener por medio de la intercesión de María “la paz entre las naciones, libertad para la Iglesia, la conversión de los pecadores, amor a la pureza y la práctica de las virtudes”. Esta fiesta se celebra en la Iglesia todos los años el sábado siguiente al segundo domingo después Pentecostés.\n\nDespués de su entrada a los cielos, el Corazón de María sigue ejerciendo a favor nuestro su amorosa intercesión.",
    "septiembre":
        "Septiembre es el mes dedicado a Nuestra Señora de los Dolores viene desde muy antiguo. Ya en el siglo VIII los escritores eclesiásticos hablaban de la “Compasión de la Virgen” en referencia a la participación de la Madre de Dios en los dolores del Crucificado.\n\nPronto empezaron a surgir las devociones a los 7 dolores de María y se compusieron himnos con los que los fieles manifestaban su solidaridad con la Virgen dolorosa.\n\nPrimer Dolor: La profecía de Simeón en la presentación del Niño Jesús\n\nSegundo Dolor: La huida a Egipto con Jesús y José\n\nTercer Dolor: La pérdida de Jesús\n\nCuarto Dolor: El encuentro de Jesús con la cruz a cuestas camino del calvario\n\nQuinto Dolor: La crucifixión y la agonía de Jesús\n\nSexto Dolor: La lanzada y el recibir en brazos a Jesús ya muerto\n\nSéptimo Dolor: El entierro de Jesús y la soledad de María",
    "octubre":
        "Octubre es el mes del Rosario y de las misiones. Del Rosario porque la Europa cristiana se vio libre de la amenaza musulmana que quería destruir el cristianismo, en el año 1571; pero fueron vencidos por las fuerzas cristianas en la Batalla de Lepanto, en el mar de Grecia.\n\nEl Papa san Pío V pidió a los ejércitos cristianos que llevaran el \'arma del Rosario\'. Como la gran y milagrosa victoria se dio el día 7 de octubre, el Papa instituyó en este día la fiesta de Nuestra Señora del Rosario.\n\nEl mes de las misiones es una devoción para estimular aún más la misión evangelizadora que Cristo confió a la Iglesia.\n\nMandó que sus discípulos fueran por todo el mundo, predicando el Evangelio y bautizando a todos.",
    "noviembre":
        "Noviembre es el mes dedicado a las almas del purgatorio.\n\nEl Día de Muertos, 2 de noviembre, está dedicado a las oraciones por todos los fieles difuntos.\n\nEl papa Pablo VI, en la \'Constitución de las Indulgencias\', de 1967, estableció indulgencias parciales y plenarias para las almas del purgatorio, y determinó la semana del 1 al 8 de noviembre como la semana de las almas, en que podemos hacer que se beneficien de las indulgencias plenarias mediante una visita al cementerio para rezar por ellas, habiéndose confesado, comulgando y rezando por el Papa (padrenuestro, ave maría, gloria al padre).\n\nLas almas, por ellas mismas no pueden conseguir su purificación; dependen de nuestras oraciones, misas, limosnas, penitencias, etc., por ellas.",
    "diciembre":
        "Diciembre es el mes de diciembre está dedicado a la Inmaculada Concepción de la Santísima Virgen María. “Desde toda la eternidad Dios eligió con infinita sabiduría a la mujer que sería la Madre de su divino Hijo. Para preparar al Verbo Encarnado un tabernáculo santo y sin mancha, Dios creó a María en gracia y la dotó desde el momento de su concepción con todos los perfecciones adecuadas a su exaltada dignidad. Santo Tomás enseña que a través de su intimidad con Cristo, principio de gracia, poseía más allá de todas las criaturas una plenitud de vida divina “. – Meditaciónes litúrgicas, Las Hermanas de Santo Domingo\n\nEsta fiesta nos invita a meditar sobre la virtud de la pureza. “María sola – ‘el alarde solitario de nuestra naturaleza contaminada’ – nunca vio la pureza de su alma oscurecida por el polvo de ninguna mancha, ni vio en ninguna parte de su camino triunfal hacia el cielo ningún pecado o rastro de mundanalidad. Por un único y singular privilegio de Dios fue preservada del pecado original desde el primer momento de su Inmaculada Concepción; por otro privilegio derivado del primero, el Señor no permitió que se manchara jamás ni siquiera con esos inevitables defectos de la debilidad humana” (Luis M. Martínez)."
}

#Devotions Link: https://rezoelrosario.com/a-que-dedica-cada-mes-la-iglesia-catolica/

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#setlocale(locale.LC_TIME, 'spanish')
#define("CHARSET", "iso-8859-1");
dt = datetime.datetime.today()

#USCCB
usccb_url = "https://bible.usccb.org/es/bible/lecturas/"+today.strftime("%m%d%y")+".cfm"
#usccb_url = "https://bible.usccb.org/es/bible/lectuars/"+today.strftime("%m%d%y")+".cfm"
r = requests.get(usccb_url)
usccb_soup = BeautifulSoup(r.content, 'html5lib')
address_table = usccb_soup.findAll('div', attrs = {'class':'address'})
content_table = usccb_soup.findAll('div', attrs = {'class':'content-body'})

#REGNUMCHRISTI: Meditación de hoy
if dt.strftime("%A") == "sÃ¡bado":
    day_of_week = "Sábado"
elif dt.strftime("%A") == "miÃ©rcoles":
    day_of_week = "Miércoles"
else:
    day_of_week = dt.strftime("%A")
#meditación_url = "https://www.regnumchristi.org/es/"+day_of_week+"-"+str(dt.day)+"-de-"+dt.strftime("%B")+"-de-"+str(dt.year)
meditación_url = "https://www.regnumchristi.org/es/viernes-30-de-julio-de-2021-es-jesus-un-hombre-ordinario/"
r = requests.get(meditación_url)
meditación_soup = BeautifulSoup(r.content, 'html5lib')
meditación_table = meditación_soup.findAll('blockquote')

#El Santo Del Día
santo_url = "https://www.santopedia.com/santoral/"+str(dt.day)+"-de-"+dt.strftime("%B")
r = requests.get(santo_url)
santo_soup = BeautifulSoup(r.content, 'html5lib')
boxList = santo_soup.findAll('a', attrs = {'class':'btn btn-mini btn-primary'})
links = [box['href'] for box in boxList]
santo_url = links[0]
r = requests.get(santo_url)
soup = BeautifulSoup(r.content, 'html5lib')
saint_page = soup.findAll('div', attrs = {'class':'saint_page'})
santo_nombre = soup.find('h1')
santo_descripcion = soup.find('div', attrs = {'class':'alert alert-info'})

url = "https://www.franciscanmedia.org/saint-of-the-day"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
images = soup.findAll('img')
santo_src = "https://www.franciscanmedia.org/"+images[4]['src']

newsletter_prayers = [
    ["Comenzar", "En el nombre del Padre, y del Hijo, y del Espíritu Santo"],
    ["Oración de la Mañana", "Oh, Jesús, a través del Inmaculado Corazón de María,\nte ofrezco mis oraciones, trabajo, alegrías, sufrimientos de este día,\nen unión al Santo Sacrificio de la Misa para el mundo.\nTe los ofrezco por los méritos de tu Sagrado Corazón:\nla salvación de las almas, enmienda de los pecados, la reunión de todos los cristianos;\nte los ofrezco por nuestros obispos y por los Apóstoles de la oración y de manera particular\npor aquellos que el Santo Padre escogió durante este mes."],
    ["Oración por el Papa Francisco", "Dios nuestro, pastor y guía de todos los fieles,\nmira con bondad a tu hijo Francisco,\na quien constituiste pastor de tu Iglesia,\ny sostenlo con tu amor,\npara que con su palabra y su ejemplo\nconduzca al pueblo que le has confiado\ny llegue, juntamente con él, a la vida eterna.\nPor nuestro Señor Jesucristo, tu Hijo,\nque vive y reina contigo en la unidad del Espíritu Santo\ny es Dios por los siglos de los siglos."],
    ["Padre Nuestro","Padre nuestro que estás en el cielo,\nsantificado sea tu Nombre;\nvenga a nosotros tu Reino;\nhágase tu voluntad\nen la tierra como en el cielo.\nDanos hoy\nnuestro pan de cada día;\nperdona nuestras ofensas,\ncomo también nosotros perdonamos\na los que nos ofenden;no nos dejes caer en la tentación,\ny líbranos del mal.",],
    ["Ave María","Dios te salve, María, llena eres de gracia, el Seńor es contigo.\nBendita tú eres entre todas las mujeres, y bendito es el fruto de tu vientre, Jesús.\nSanta María, Madre de Dios,\nruega por nosotros, pecadores,\nahora y en la hora de nuestra muerte."],
    ["Gloria al Padre", "Gloria al Padre\ny al Hijo\ny al Espíritu Santo.\nComo era en el principio,\nahora y siempre,\npor los siglos de los siglos."],
    #["Meditación Diaria", meditación_table[0].text.strip()],
    #["El Santo Del Día", saint_nombre + saint_descripcion],
    #["Devoción del Mes",devociónes[dt.strftime("%B")]],
    #["Lecturas de Hoy",""],
    #["Lectura I", content_table[0].text.strip() + "\n\n" + address_table[0].text.strip()],
    #["Salmo Responsorial", content_table[1].text.strip() + "\n\n" + address_table[1].text.strip()],
    #["Evangelio", content_table[3].text.strip() + "\n\n" + address_table[2].text.strip()],
    ["Comunión Espiritual","Jesús mío,\ncreo que estás real y verdaderamente en el Cielo\ny en el Santísimo Sacramento del altar.\nTe amo por sobre todas las cosas\ny deseo vivamente recibirte dentro de mi alma,\npero no pudiendo hacerlo ahora sacramentalmente,\nven al menos espiritualmente a mi corazón.\nY como si ya te hubiese recibido,\nTe abrazo y me uno del todo a Ti.\nSeñor, no permitas que jamás me aparte de Ti. Amén."],
    ["Consagración a María", "Bendita sea tu pureza\ny eternamente lo sea,\npues todo un Dios se recrea\nen tan graciosa belleza.\nA ti, celestial Princesa,\nVirgen sagrada Maria,\nte ofrezco desde este día\nalma, vida y corazón.\nMírame con compasión,\nno me dejes, Madre mía, \nahora y en mi última agonía."],
    ["Oración a San José", "Glorioso patriarca San José,\ncuyo poder sabe hacer posibles las cosas imposibles,\nen en mi ayuda en estos momentos de angustia y dificultad.\n\nToma bajo tu protección las situaciones\ntan graves y difíciles que te confío,\npara que tengan una buena solución.\n\nMi amado Padre,\ntoda mi confianza está puesta en ti.\nQue no se diga que te haya invocado en vano\ny, como puedes hacer todo con Jesús y María,\nmuéstrame que tu bondad es tan grande como tu poder."],
    ["Oración al ángel de mi guarda", "Ángel de mi guarda,\ndulce compañía,\nno me desampares,\nni de noche ni de día,\nno me dejes solo, que me perdería,\nhasta que me pongas, en paz y alegría,\ncon todos los santos, Jesús y María,\nte doy el corazón y el alma mía\nque son mas tuyos que míos."],
    ["Oración a san Miguel arcángel", "San Miguel Arcángel,\ndefiéndenos en la batalla.\nSé nuestro amparo\ncontra las perversidad y asechanzas\ndel demonio.\nReprímale Dios, pedimos suplicantes,\ny tu príncipe de la milicia celestial\narroja al infierno con el divino poder\na Satanás y a los otros espíritus malignos\nque andan dispersos por el mundo\npara la perdición de las almas."],
    ["Acabar", "En el nombre del Padre, y del Hijo, y del Espíritu Santo. \nAmén."]
]


#NEWSLETTER---------------------------------------------------------------------
template = open('newsletter_template.html')
soup = BeautifulSoup(template.read(), "html.parser")

newsletter_content = ""

#Header-------------------------------------------------------------------------
header_template = soup.find('header', attrs={'class':'section'})
title = header_template.h1
title.string = day_of_week.capitalize() +", "+str(dt.day)+" de "+dt.strftime("%B").capitalize() +" "+str(dt.year)
newsletter_content += str(header_template)

#Meditación---------------------------------------------------------------------
article_template = soup.find('section', attrs={'class':'section'})
title = article_template.h2
title.string = "Meditación Diaria"
subtitle = article_template.p
med_string = meditación_table[0].text.strip().replace("«", "")
med_string = med_string.replace("»", "")
subtitle.string = med_string
newsletter_content += str(article_template)

#Lecturas de Hoy Header--------------------------------------------------------
title.string = "Lecturas de Hoy"
subtitle.string = ""
img = article_template.img
img['src'] = "images/misa.jpg"
article_template.img.replace_with(img)
newsletter_content += str(article_template)
###
lecturas_template = soup.find('lectura', attrs={'class':'section'})
#lectura 1
subheading = lecturas_template.h3
subheading.string = "Lectura I"
subtitle = lecturas_template.p
subtitle.string = content_table[0].text.strip()
address = lecturas_template.em
address.string = address_table[0].text.strip()
newsletter_content += str(lecturas_template)
#Salmo Responsorial
subheading.string = "Salmo Responsorial"
subtitle = lecturas_template.p
subtitle.string = content_table[1].text.strip()
address = lecturas_template.em
address.string = address_table[1].text.strip()
newsletter_content += str(lecturas_template)
#Evangelio
if dt.strftime("%A") == "domingo":
    #LECTURA 2
    subheading.string = "Lectura II"
    subtitle = lecturas_template.p
    subtitle.string = content_table[2].text.strip()
    address = lecturas_template.em
    address.string = address_table[2].text.strip()
    newsletter_content += str(lecturas_template)
    #Evangelio
    subheading.string = "Evangelio"
    subtitle = lecturas_template.p
    subtitle.string = content_table[4].text.strip()
    address = lecturas_template.em
    address.string = address_table[4].text.strip()
    newsletter_content += str(lecturas_template)
else:
    subheading.string = "Evangelio"
    subtitle = lecturas_template.p
    subtitle.string = content_table[3].text.strip()
    address = lecturas_template.em
    address.string = address_table[3].text.strip()
    newsletter_content += str(lecturas_template)

#El Santo Del Día-----------------------------------------------------------------------
title.string = "Santo Del Día: " + santo_nombre.text
subtitle = article_template.p
subtitle.string = santo_descripcion.text
img = article_template.img
img['src'] = santo_src
article_template.img.replace_with(img)
newsletter_content += str(article_template)
#empty image
img = article_template.img
img['src'] = ""
article_template.img.replace_with(img)

#Devoción-----------------------------------------------------------------------
title.string = "Devoción del Mes"
subtitle = article_template.p
subtitle.string = devociónes[dt.strftime("%B")]
img = article_template.img
img['src'] = "images/devociones/"+dt.strftime("%B")+".jpg"
article_template.img.replace_with(img)
newsletter_content += str(article_template)
#empty image
img = article_template.img
img['src'] = ""
article_template.img.replace_with(img)

#Prayers-----------------------------------------------------------------------
title.string = "Oraciones Diarias"
subtitle.string = ""
img = article_template.img
img['src'] = ""
article_template.img.replace_with(img)
newsletter_content += str(article_template)

prayers_template = soup.find('prayers', attrs={'class':'section'})

for i in range(len(newsletter_prayers)):
    title = prayers_template.p
    title.string = newsletter_prayers[i][0]

    subtitle = prayers_template.h3
    subtitle.string = newsletter_prayers[i][1]

    newsletter_content += str(prayers_template)#.replace('\n','')

#Footer-------------------------------------------------------------------------
footer_template = soup.find('footer', attrs={'class':'section'})
title = footer_template.h2
title.string = day_of_week.capitalize() +", "+str(dt.day)+" de "+dt.strftime("%B").capitalize() +" "+str(dt.year)
newsletter_content += str(footer_template)

html_start = str(soup)[:str(soup).find(str(header_template))]
#html_end = str(soup)[str(soup).find(str(header_template))+len(str(header_template)):]
html_start = html_start.replace('\n','')
#html_end = html_end.replace('\n','')

#EMAIL---------------------------------------------------------------------------
email_content = html_start + newsletter_content #+ html_end
open('newsletter_today.html', 'w').close()
newsletter_today = open("newsletter_today.html", "a", encoding='utf-8')
newsletter_today.write(email_content)
newsletter_today.close()

#SITE---------------------------------------------------------------------------
site_template = open('site_template.html',mode='r')
site_template_text = site_template.read()
site_template.close()

site_content = site_template_text + newsletter_content  + "</body></div></div></html>"
open('site_today.html', 'w').close()
site_today = open("site_today.html", "a", encoding='utf-8')
site_today.write(site_content)
site_today.close()

#CREATE PAGE FOR ARCHIVE--------------------------------------------------------
achive_page = open('archive/'+today.strftime("%m%d%y")+'.html','w', encoding='utf-8')
achive_page.write(site_content)
achive_page.close()

#APPEND TO ARCHIVE--------------------------------------------------------------
archive_list = open("archive.html", "a", encoding='utf-8')
archive_list.write('<li><a href='+'\'/newsletter_content/archive/'+today.strftime("%m%d%y")+'.html\'>'+str(dt.day)+"-de-"+dt.strftime("%B")+"-de-"+str(dt.year)+'</a></li>')
archive_list.close()

#CHECK
#print(BeautifulSoup(site_content).prettify())
