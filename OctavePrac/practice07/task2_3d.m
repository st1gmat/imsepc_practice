##x = -pi:0.1:pi;
##y = -pi:0.1:pi;
##
##[X, Y] = meshgrid(x, y);
##z = 20 - X.^2 - Y.^2;
##
##[u, v, w] = surfnorm(X, Y, z/10);
##hold on;
##h = quiver3(X, Y, z, u, v, w);
##set (h, "maxheadsize", 0.25);
##hold off;

x = -pi:0.1:pi;
y = -pi:0.1:pi;
[X, Y] = meshgrid(x, y);
z = 20 - X.^2 - Y.^2;

surf(X, Y, z)

colormap("spring")
shading interp
axis equal

x0 = 0;
y0 = -1;


z0 = 20 - x0^2 - y0^2;

h = 10^(-10);

dx = ((x0 + h)^2 - x0^2)/h;
dy = ((y0 + h)^2 - y0^2)/h;
dz = ((z0 + h) - z0)/h;

t = -1:0.03:1;
ax = dx*t + x0;
ay = dy*t + y0;
az = dz*t + z0;

hold on
plot3(ax, ay, az)
hold off



##[dx, dy] = gradient(x, y);
## nx = -dx;
## ny = -dy;
## nz = ones(size(dx));
## mag = sqrt(nx.^2 + ny.^2 + nz.^2);
## nx = nx ./ mag;
## ny = ny ./ mag;
## nz = nz ./ mag;

##quiver3(X, Y, z, nx, ny, nz);

##x = -pi:0.1:pi;
##y = -pi:0.1:pi;
##x0 = 0;
##y0 = -1;
##h = 10^(-9)
##
##
####z = 20 - X.^2-Y.^2;
##
####f = z - 20 + X.^2 + Y.^2;
##z0 = 20 - x0^2 - y0^2;
##dx = ((20 - (x0+h)^2-y0^2 - z0) - (20 - x0^2 - y0^2 - z0));
##dy = ((20 - x0^2-(y0+h)^2 - z0) - (20 - x0^2 - y0^2 - z0));
##dx = ((20 - x0^2 - y0^2 - (z0+h)) - (20 - x0^2 - y0^2 - z0));
##
##diffX = lim(dx/h, h, 0);
##diffY = lim(dy/h, h, 0);
##diffZ = lim(dz/h, h, 0);
##
##
##
##surf(diffX, diffY, diffZ)
