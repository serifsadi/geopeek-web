// Single source for release facts. Update on each release.
// The DMG version and URL point at the v1.0.0 launch asset. Checked 2026-11-27:
// GitHub has no v1.0.0 release yet. dmgSize and released stay the verified
// v0.4.1 figures (2,780,712 bytes, published 2026-11-23). Recheck both before launch.
export const SITE = {
  url: 'https://geopeek.app',
  name: 'GeoPeek',
  version: '1.0.0',
  released: '2026-11-23',
  dmgName: 'GeoPeek-1.0.0.dmg',
  dmgUrl: 'https://github.com/serifsadi/geopeek/releases/download/v1.0.0/GeoPeek-1.0.0.dmg',
  dmgSize: '2.8 MB', // 2,780,712 bytes on v0.4.1; recheck GeoPeek-1.0.0.dmg before launch
  releasesUrl: 'https://github.com/serifsadi/geopeek/releases',
  releaseNotesUrl: 'https://github.com/serifsadi/geopeek/releases/tag/v1.0.0',
  macAppStoreUrl: 'https://apps.apple.com/app/id6839084436',
  repoUrl: 'https://github.com/serifsadi/geopeek',
  issuesUrl: 'https://github.com/serifsadi/geopeek/issues',
  newIssueUrl: 'https://github.com/serifsadi/geopeek/issues/new',
  licenseUrl: 'https://github.com/serifsadi/geopeek/blob/main/LICENSE',
  changelogUrl: 'https://github.com/serifsadi/geopeek/blob/main/CHANGELOG.md',
  brew: 'brew install --cask serifsadi/geopeek/geopeek',
  brewTrust: 'brew trust --cask serifsadi/geopeek/geopeek',
  minMacOS: '15.0',
  author: 'Şerif Şadi Şenkule',
  authorUrl: 'https://serifsadi.dev',
} as const;
