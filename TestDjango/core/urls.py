from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.Carrito import Carrito
#from TestDjango.core.models import Producto
#from TestDjango.core.models import Arriendo,Reparacion



from .views import Arbusto, agregar_producto, eliminar_producto, form_arriendo, listado_arriendo, registro,home, Contacto,\
    Categoria1, F_Crear_Cuenta,form_mod_usuario,Nosotros,HistoricoCompra,index_home,InicioSesion1,\
    limpiar_carrito,listado_producto, Paypal,PerfilProducto,Producto1,Seguimiento,Tierra,\
    Macetero,index_homeOG, form_usuario,restar_producto, form_producto, Carrito,\
    form_mod_producto,form_borrar_producto,listado_usuario, form_borrar_usuario,\
    P_Arriendo,Servicios_M,P_Promociones,Admin_E_Servicios,listado_arriendo,form_arriendo,form_mod_arriendo,form_reparacion,DashBoard,form_producto_arriendo,bicicleta_perso
# ,NavBar
    

urlpatterns = [
    path('home1',home , name="Home"),
    path('', index_home, name="index_home"),
    path('Repuestos y accsesorios/', Arbusto, name="Arbusto"),
    path('home/',index_homeOG , name="home"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Categoria1/', Categoria1, name="Categoria1"),
    path('F_Crear_Cuenta/', F_Crear_Cuenta, name="F_Crear_Cuenta"),
    path('form_mod_usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form_usuario/', form_usuario, name="form_usuario"),
    path('form_producto/', form_producto, name="form_producto"),
    path('form_producto_arriendo/', form_producto_arriendo, name="form_producto_arriendo"),

    path('login',Carrito),
    path('P_Arriendo/', P_Arriendo, name="P_Arriendo"),
    path('Servicios_M/', Servicios_M, name="Servicios_M"),
    path('HistoricoCompra/', HistoricoCompra, name="HistoricoCompra"),

    path('P_Promociones/', P_Promociones, name="P_Promociones"),
    path('Admin_E_Servicios/', Admin_E_Servicios, name="Admin_E_Servicios"),
    #path('Home/', index_home, name="Home"),
    path('InicioSesion1/', InicioSesion1, name="InicioSesion1"),
    path('listado_producto/', listado_producto, name="listado_producto"),
    path('listado_usuario/', listado_usuario, name="listado_usuario"),
    path('registro',registro, name="registro"),
    path('Bicicletas/', Macetero, name="Macetero"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('Paypal/', Paypal, name="Paypal"),
    path('PerfilProducto/<id>', PerfilProducto, name="PerfilProducto"),
    path('Producto/', Producto1, name="Producto"),
    path('Seguimiento/', Seguimiento, name="Seguimiento"),
    path('Mantenciones/', Tierra, name="Tierra"),
    #path('Nav/', NavBar, name="Nav"),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="sub"),
    path('limpiar/', limpiar_carrito, name="cls"),
    path('form_mod_producto/<id>/', form_mod_producto, name="form_mod_producto"),
    path('form_borrar_producto/<id>/',form_borrar_producto, name="form_borrar_producto"),
    path('form_borrar_usuario/<id>/',form_borrar_usuario, name="form_borrar_usuario"),
    path('listado_arriendo',listado_arriendo, name="listado_arriendo"),
    path('form_arriendo',form_arriendo, name="form_arriendo"),
    path('form_mod_arriendo',form_mod_arriendo, name="form_mod_arriendo"),
    path('form_reparacion',form_reparacion, name="form_reparacion"),
    path('DashBoard',DashBoard, name="DashBoard"),
    path('bicicleta_perso',bicicleta_perso, name="bicicleta_perso"),

]


urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
