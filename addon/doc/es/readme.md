# UnicodeBrailleInput #

* Autores: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* descargar [versión estable][1]

Este complemento te permite convertir texto de braille
(P.e.. 1345-1236-145-1) a caracteres braille Unicode. También puedes
convertir texto utilizando la tabla de entrada Braille seleccionada
actualmente.

El propósito de este complemento especializado es hacer más fácil el ayudar
a mejorar las tablas de liblouis y añadir pruebas automáticas para tu
idioma. Con la incorporación de tablas braille unicode en NVDA 2017.3, este
complemento ya no se requiere para esto, ya que los usuarios pueden elegir
introducir braille con la tabla nueva. Sin embargo, este complemento todavía
puede ayudar a convertir texto normal en Braille Unicode según una tabla
particular de entrada.

## Utilización

* Abrir un editor de textos que soporte unicode (por ejemplo Notepad más
  más).
* Pulsa NVDA+Ctrl+U o elige Entrada de Braille Unicode encontrada en el menú
  herramientas de NVDA.
* Elige si tu entrada consta de puntos Braille (p.e. 1345-1236-145-1) o
  texto normal según la tabla Braille actual (p.e. holandés).
* Escribir el texto braille en forma numérica o texto normal,
  respectivamente.
* Pulsar Aceptar.
* Los caracteres Unicode se copiarán en el portapapeles listos para pegarse.

## Cambios para 3.0

* Nuevo responsable de mantenimiento: Leonard de Ruijter.
* El complemento es compatible con Python 3 y, por lo tanto, con NVDA 2019.3
  y posterior.
* Añadida la capacidad de crear Braille Unicode a partir de texto normal
  siguiendo la tabla de entrada Braille seleccionada.

## Cambios para 2.0

* La ayuda del complemento está disponible en el Administrador de
  Complementos.

## Cambios para 1.1 ##

* Mejora el retraso para permetir que los anuncios se escuchen
  correctamente.
* Muchas traducciones nuevas .
* Documentación incluida en el menú de ayuda de NVDA .
* Se ha añadido una opción para, opcionalmente, reemplazar el espacio
  braille (carácter 0x2800) por el carácter de espacio regular.
* Los Atajos de teclado ahora pueden ser reasignados utilizando el diálogo
  Gestos de Entrada de NVDA, en la categoría de Herramientas.

## Cambios para 1.0 ##

* Versión inicial
* Nuevos idiomas: Francés

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
