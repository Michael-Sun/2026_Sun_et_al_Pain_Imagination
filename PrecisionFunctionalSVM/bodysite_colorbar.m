function bodysite_colorbar()
    % CREATE_HORIZONTAL_COLORBAR Generates a horizontal colorbar with specified properties.

    % Define body site names
    bodysite_names = {... 
        'Left Face', ...
        'Right Face', ...
        'Left Arm', ...
        'Right Arm', ...
        'Left Leg', ...
        'Right Leg', ...
        'Chest', ...
        'Abdomen'};

    % if nargin < 1
    %     orientation = 'eastoutside'; % default: vertical on the right
    % end

    % Define colormap
    cmap = [
        0.5, 0.5, 0.5;
        0.85, 0.33, 0.10; % Left Face (Red)
        1.00, 0.41, 0.16; % Right Face (Lighter Red)
        0.00, 0.45, 0.74; % Left Arm (Blue)
        0.30, 0.75, 0.93; % Right Arm (Lighter Blue)
        0.47, 0.67, 0.19; % Left Leg (Green)
        0.60, 0.87, 0.54; % Right Leg (Lighter Green)
        0.93, 0.69, 0.13; % Chest (Orange)
        0.49, 0.18, 0.56; % Abdomen (Purple)
    ];

    % Create a new figure and turn off axes
    % figure;
    axis off;

    % Apply the colormap
    colormap(cmap);

    % Create the colorbar
    cb = colorbar;
    % cb.Location = orientation;

    % cb.Position = cb.Position + 1e-10;

    % Set the colorbar to be horizontal
    cb.Location = 'eastoutside';


    % Set the limits of the colorbar to the number of colors (1 to 8)
    % Note: This ensures no distortion in the mapping
    % caxis([1, 8]);

    % Set the limits of the colorbar to match the number of colors (1 to 8)
    % cb.Limits = [1, 8];

    % Define tick positions at midpoints of each color section
    % tickPositions = linspace(1 / (2 * 8), 1 - 1 / (2 * 8), 8);
    % Define tick positions to align with categories 2 to 8
    tickPositions = linspace(2.5, 9.5, 8); % Midpoints of categories 2 to 8


    % Set ticks and labels
    cb.Ticks = tickPositions;
    cb.TickLabels = bodysite_names;

    % Set colorbar label
    cb.Label.String = 'Body Sites';

    % cb.Location = orientation;
end


% function bodysite_colorbar(orientation)
%     % BODYSITE_COLORBAR  Categorical colorbar for 8 body sites.
%     %
%     %   bodysite_colorbar          -> vertical bar (right)
%     %   bodysite_colorbar('southoutside') -> horizontal bar
% 
%     if nargin < 1
%         orientation = 'eastoutside'; % default: vertical on the right
%     end
% 
%     % Body site names
%     bodysite_names = { ...
%         'Left Face', ...
%         'Right Face', ...
%         'Left Arm', ...
%         'Right Arm', ...
%         'Left Leg', ...
%         'Right Leg', ...
%         'Chest', ...
%         'Abdomen'};
% 
%     % Colormap (8 distinct colors)
%     cmap = [
%         0.85, 0.33, 0.10; % Left Face (Red)
%         1.00, 0.41, 0.16; % Right Face (Lighter Red)
%         0.00, 0.45, 0.74; % Left Arm (Blue)
%         0.30, 0.75, 0.93; % Right Arm (Lighter Blue)
%         0.47, 0.67, 0.19; % Left Leg (Green)
%         0.60, 0.87, 0.54; % Right Leg (Lighter Green)
%         0.93, 0.69, 0.13; % Chest (Orange)
%         0.49, 0.18, 0.56; % Abdomen (Purple)
%     ];
% 
%     % New figure and invisible axes
%     figure('Color','w');
%     ax = axes('Position',[0.1 0.1 0.1 0.8], 'Visible','off'); %#ok<LAXES>
% 
%     % Dummy image with values 1..8
%     % imagesc(ax, (1:8)');          % 8-by-1 image
%     % colormap(ax, cmap);
%     ax.CLim = [0.5 8.5];          % so each integer maps to one color
%     ax.YTick = []; ax.XTick = [];
% 
%     % Colorbar attached to this axes
%     cb = colorbar(ax, orientation);
%     cb.Ticks      = 1:8;
%     cb.TickLabels = bodysite_names;
%     cb.Label.String = 'Body Sites';
% 
%     % Optional cosmetics
%     cb.TickDirection = 'out';
% 
%     % Apply the colormap
%     colormap(cmap);
% end
