# Очень часто изображения обрабатываются как массив RGB-пикселей. Хотя эта идея кажется
# относительно интуитивной, она не оптимальна для решаемой нами задачи.
# В RGB цвет пикселя определяется насыщенностью красного, зеленого и синего.
# Таким образом, выбор диапазона оттенков одного цвета становится не самой простой задачей.
# Иначе обстоит дело с форматом HSV. Эта цветовая схема определяется тремя компонентами:
# Hue - цветовой тон;
# Saturation - насыщенность;
# Value - яркость.
# В схеме HSV базовый цвет можно выбрать с помощью компоненты Hue (например, красный, оранжевый и т.д.).
# Две другие компоненты позволяют регулировать насыщенность и яркость базового цвета,
# делая его более насыщенным или блеклым, светлее или темнее.
# Эти свойства HSV позволяют легко определять диапазоны, которые могут захватывать области нужного цвета и его оттенков.

import cv2
import numpy as np

# Указываем полный путь к файлу (изображению) или
# имя файла, если он сохранен в папке проекта
image = cv2.imread("11zadan.jpg")

# Создаем окно. Выводим изображение. Подписываем окно
cv2.imshow("original", image) 

# Ждем нажатия клавиши для перехода к следующей команде
cv2.waitKey(0)

# Библиотека Open CV может делать различные операции с изображением

# Добавляем размытие для подавления шумов
blurred_image = cv2.GaussianBlur(image, (11, 11), 0)

# Создаем окно. Выводим изображение. Подписываем окно
cv2.imshow("blurred", blurred_image)

# Ждем нажатия клавиши для перехода к следующей команде
cv2.waitKey(0)

# Изменяем цветовую палитру (конвертируем RGB в HSV)
hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

# Создаем окно. Выводим изображение. Подписываем окно
cv2.imshow("hsv", hsv_image)

# Ждем нажатия клавиши для перехода к следующей команде
cv2.waitKey(0)

# Устанавливаем границы цвета для зеленого
hsv_min = np.array((36, 25, 25), np.uint8)  # Нижняя граница зеленого цвета
hsv_max = np.array((70, 255, 255), np.uint8)  # Верхняя граница зеленого цвета

# Создаем маску с границами. Выделяем область
green_mask = cv2.inRange(hsv_image, hsv_min, hsv_max)

# Создаем окно. Выводим изображение. Подписываем окно
cv2.imshow("mask", green_mask)

# Ждем нажатия клавиши для перехода к следующей команде
cv2.waitKey(0)

# Метод findContours находит контуры и возвращает их вместе с иерархией
#                              передаем копию объекта; алгоритм поиска; алгоритм аппроксимации контуров
contours, hierarchy = cv2.findContours(green_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Сортируем все найденные контуры по убыванию площади
sorted_contur = sorted(contours, key=cv2.contourArea, reverse=True)

# Find the largest object - берем первый (самый большой) контур
if len(sorted_contur) > 0:
    # Determine the coordinates of the largest object
    x, y, w, h = cv2.boundingRect(sorted_contur[0])
    
    print(f"Largest object: x={x}, y={y}, width={w}, height={h}")
    
    # Determine the center of the largest object
    center_x = x + w // 2
    center_y = y + h // 2
    print(f"Center coordinates: ({center_x}, {center_y})")
    
    # Outline the largest object with a red frame
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    
    # Draw the center point
    cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)
    
    # Add text with coordinates
    cv2.putText(image, f"Center: ({center_x}, {center_y})", 
                (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
else:
    print("No objects found")

# Создаем окно. Выводим изображение. Подписываем окно
cv2.imshow('Largest Object Detection', image)

# Ждем нажатия клавиши для перехода к следующей команде
cv2.waitKey(0)
cv2.destroyAllWindows()
