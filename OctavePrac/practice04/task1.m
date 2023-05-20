%{
function M = eazypeazy(n, r)
M = zeros(n);

cx = (n+1)/2;
cy = (n+1)/2;

for i=1:n
    for j=1:n
        dist = sqrt((i-cx)^2 + (j-cy)^2);
        if dist <= r
            M(i,j) = 1;
        end
    end
end
%}


%}
function M = zigzag(n)
    M = zeros(n,n);
    states = 1:4; #
    x = 1;
    y = n;
    state = 1;
    for i = 1:(n*n)
        if x!=0 && y!=0
          M(y, x) = i
        elseif x==0 && y!=0
          x++
          M(y, x) = i
        elseif x !=0 && y ==0
          y++
          M(y, x) = i
        elseif y>n
            y--
            M(y, x) = i
        elseif x>n
            x--
            M(y, x) = i
        endif
        if state == 1
            x++
            if y==1
                state = states(4)
            else
                state = states(3)
            endif
        elseif state == 2
            --y
            if x==1
                state = states(4)
            else
                state = states(3)
            end
        elseif state == 3
            x--
            y--
            if x==1
                state = states(2)
            elseif y==1
                state = states(1)
            end
        elseif state == 4
            x++
            y++
            if y == n
                state = states(1)
            elseif x == n
                state = states(2)
            end
        end
    endfor
    rot90(M, 2)
end
%{
function A = zigzag(n)
    A = zeros(n);
    count = 1;
    for i = 1:n
        if mod(i, 2) == 1
            for j = 1:i
                A(j, i - j + 1) = count;
                count = count + 1;
            end
        else
            for j = 1:i
                A(i - j + 1, j) = count;
                count = count + 1;
            end
        end
    end
end

%{
function A = randdiap(n, diap1, diap2)

end

%}


%{
function M = zz(N)
    count = 1;
    M = zeros(N)
    for d = 1:N+N
        for i = 1:N
            for j=1:N
                if i+j == d
                    M(i,j)=count
                    count = count + 1
                endif
            endfor
        endfor
    endfor
end
%}
