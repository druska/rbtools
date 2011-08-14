        # Store the 'correct' way to invoke git, just plain old 'git' by
        # default.
            if (sys.platform.startswith('win') and
                check_install('git.cmd --help')):
        self.bare = execute([self.git, "config",
                             "core.bare"]).strip() == 'true'
        self.head_ref = execute([self.git, 'symbolic-ref', '-q',
                                 'HEAD']).strip()
                            m = re.search(r'^Remote Branch:\s*(.+)$', data,
                                          re.M)
                                sys.stderr.write('Failed to determine SVN '
                                                 'tracking branch. Defaulting'
                                                 'to "master"\n')
        upstream_branch = (self._options.tracking or
                           default_upstream_branch or
                           'origin/master')
        return ((actual[0] > expected[0]) or
                (actual[0] == expected[0] and actual[1] > expected[1]) or
                (actual[0] == expected[0] and actual[1] == expected[1] and
                 actual[2] >= expected[2]))
        self.merge_base = execute([self.git, "merge-base",
                                   self.upstream_branch,
            self._options.summary = execute([self.git, "log",
                                             "--pretty=format:%s",
                                             "HEAD^.."],
                                            ignore_errors=True).strip()
            diff_lines = execute([self.git, "diff", "--no-color",
                                  "--no-prefix", "--no-ext-diff", "-r", "-u",
                                  rev_range],
                # Add the following so that we know binary files were
                # added/changed.
        self.merge_base = execute([self.git, "merge-base",
                                   self.upstream_branch,
                parent_diff_lines = self.make_diff(self.merge_base,
                                                   revision_range)
                    [self.git, "log", "--pretty=format:%s",
                     revision_range + ".."],
            if (self._options.guess_description and
                not self._options.description):
                    [self.git, "log", "--pretty=format:%s%n%n%b",
                     revision_range + ".."],
                    [self.git, "log",
                     "--pretty=format:%s", "%s..%s" % (r1, r2)],
            if (self._options.guess_description and
                not self._options.description):
                    [self.git, "log", "--pretty=format:%s%n%n%b",
                     "%s..%s" % (r1, r2)],