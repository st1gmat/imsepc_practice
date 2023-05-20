function matr = matchange(n, m)
  #matr = zeros(n, m);
  matr = false(n,m)
  #matr(:, 2:2:m) = 1;
  matr(:, 2:2:m) = true;
end
