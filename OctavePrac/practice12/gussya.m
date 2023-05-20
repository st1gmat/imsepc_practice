clear, clc
##x=0:pi/50:4*pi;
##y=sin(x)+1;
####[X,Y]=meshgrid(x,y);
####plot(y);
##
##guss =
##drawCircle(5, 5, 10)
# создать анимацию гусеницы которая ползет по синусоиде, гусеница состоит из окружностей количества n, на octave
##t = 0:0.1:10*pi;
##x = 5*sin(t);
##y = 5*cos(t);
##for i = 1:length(t)
##    plot(x(i), y(i), 'o', 'MarkerSize', 20);
##    axis([-6 6 -6 6]);
##    drawnow; % обновляем график
##    pause(0.05); % задержка для создания эффекта движения
##end

n = 5;
A = 1;
T = 2*pi; ## период синусоиды
speed = 0.01;

angles = linspace(0, 2*pi, n+1); # углы для построения окружностей
radii = ones(1, n+1); #радиусы окружностей
x = radii .* cos(angles);
y = radii .* sin(angles);
#
figure('color', 'w');
h = plot(y, x, 'o', 'MarkerSize', 15);
axis([-4 4 -300 300]);

for t = 0:0.01:10*pi

    new_x = x + A*sin((2*pi/T)*y + t);
    new_y = y;


    set(h, 'XData', new_y, 'YData', new_x);
    drawnow


    pause(speed);

    x = new_x;
    y = new_y;
end


##% Настройки
##n = 10; % количество окружностей, из которых состоит гусеница
##A = 1; % амплитуда синусоиды
##T = 2*pi; % период синусоиды
##speed = 0.1; % скорость движения гусеницы
##
##% Создаем окружности
##angles = linspace(0, 2*pi, n+1); % углы для построения окружностей
##radii = ones(1, n+1); % радиусы окружностей
##x = radii .* cos(angles); % координаты x для окружностей
##y = radii .* sin(angles); % координаты y для окружностей
##
##% Создаем фигуру
##figure('color', 'w');
##h = plot(x, y, 'o', 'MarkerFaceColor', 'k', 'MarkerSize', 20);
##axis([-1.5 1.5 -1.5 1.5]); % ограничиваем область построения
##
##% Анимация
##for t = 0:0.01:10*pi
##    % Вычисляем новые координаты для окружностей
##    new_x = x + A*sin((2*pi/T)*y + t);
##    new_y = y;
##
##    % Обновляем фигуру
##    set(h, 'XData', new_x, 'YData', new_y);
##    drawnow;
##
##    % Задержка для создания эффекта движения
##    pause(speed);
##
##    % Обновляем координаты для следующей итерации
##    x = new_x;
##    y = new_y;
##end
##
##
##
##

