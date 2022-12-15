import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Cuando los mensajeros de Juan se alejaron, Jesús se puso
         a hablar de Juan a la gente: «¿Qué salisteis a ver en el desierto?
          ¿Una caña agitada por el viento? ¿Qué salisteis a ver, si no?
           ¿Un hombre elegantemente vestido? ¡No! Los que visten magníficamente y viven
            con molicie están en los palacios. Entonces, ¿qué salisteis a ver? ¿Un profeta?
             Sí, os digo, y más que un profeta. Éste es de quien está escrito:
              ‘He aquí que envío mi mensajero delante de ti, que preparará por delante
               tu camino’. Os digo: Entre los nacidos de mujer no hay ninguno mayor que Juan;
                sin embargo el más pequeño en el Reino de Dios es mayor que él».
        """, classes="text-lg")
        return wp


