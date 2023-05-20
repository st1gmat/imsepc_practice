##Есть комплекснозначная функция z^3 -1 у которой три корня, z0 с помощью метода ньютона перебираем значения в прямоугольнике о т -2 до 2,
##если z0  сошлось к 1ому корню закрашиваем в один цвет, если ко второму в др. и к 3ьему в третий, если не сошлось то в 4ый. Использовать функцию image

clear;
f = @(z) z^3 - 1;

x_min = -2;
x_max = 2;
y_min = -2;
y_max = 2;

n_points = 50;

[x, y] = meshgrid(linspace(x_min, x_max, n_points), linspace(y_min, y_max, n_points));

eps = 1e-3;
z = zeros(size(x));

for i = 1:numel(x)
    z0 = x(i) + 1i*y(i);
    root = rootNewton(f, z0);

    if abs(root(1) - 1) < eps
        z(i) = 1;
    elseif abs(root(2) - exp(2i*pi/3)) < eps
        z(i) = 2;
    elseif abs(root(3) - exp(4i*pi/3)) < eps
        z(i) = 3;
    else
        z(i) = 4;
    end
end

image(x_min:x_max, y_min:y_max, z);
colormap([1 0 0; 0 1 0; 0 0 1; 0 0 0]);
axis equal;

