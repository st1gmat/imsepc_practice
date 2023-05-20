x = linspace(-2, 2, 20)
y=x';
z = x.*exp(-x.^2-y.^2)
%{
plot(x, y, 'LineWidth', 3, 'Color', 'm')

%}
plot(x, y, 'LineWidth', 3, 'Color', 'm')
surf(x, y, z)
grid on
%{

xlabel('x')
ylabel('y')
%}

title('Magic')
